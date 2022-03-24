#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <byteswap.h>
#include <string.h>
#include <errno.h>
#include <signal.h>
#include <fcntl.h>
#include <ctype.h>
#include <termios.h>
#include <math.h>
#include <sys/types.h>
#include <sys/mman.h>

/* ltoh: little to host */
/* htol: little to host */
#if __BYTE_ORDER == __LITTLE_ENDIAN
#  define ltohl(x)       (x)
#  define ltohs(x)       (x)
#  define htoll(x)       (x)
#  define htols(x)       (x)
#elif __BYTE_ORDER == __BIG_ENDIAN
#  define ltohl(x)     __bswap_32(x)
#  define ltohs(x)     __bswap_16(x)
#  define htoll(x)     __bswap_32(x)
#  define htols(x)     __bswap_16(x)
#endif
  
#define FATAL do { fprintf(stderr, "Error at line %d, file %s (%d) [%s]\n", __LINE__, __FILE__, errno, strerror(errno)); exit(1); } while(0)
 
/*#define MAP_SIZE (32*1024UL)*/
#define MAP_SIZE (32*49152UL)
#define MAP_MASK (MAP_SIZE - 1)

int main(int argc, char **argv) {
  int fd;
  void *map_base, *virt_addr; 
  uint32_t read_result, writeval;
  off_t target;
  /* access width */
  int access_width = 'w';
  char *device;
  float WNS = 0;
  float cal_clk = 100;
  float original_period = 0;
  float scaled_period = 0;
  float scaled_clk = 0;
  float DIVCLK_DIVIDE;
  float CLKFBOUT_MULT;
  float CLKOUT0_DIVIDE;
  int i = 1;
  int j = 16;
  int k = 8;
  float temp_clk;

  /* not enough arguments given? */
  if (argc < 3) {
    fprintf(stderr, "\nUsage:\t%s <device> <address> [[type] data]\n"
      "\tdevice  : character device to access\n"
      "\taddress : memory address to access\n"
      "\ttype    : access operation type : [b]yte, [h]alfword, [w]ord\n"
      "\tdata    : data to be written for a write\n\n",
      argv[0]);
    exit(1);
  }

  printf("argc = %d\n", argc);
  printf("Used API: %s\n", argv[0]);
  device = strdup(argv[1]);
  printf("device: %s\n", device);
  target = strtoul(argv[2], 0, 0);
  printf("address: 0x%08x\n", (unsigned int)target);

  printf("access type: %s\n", argc >= 4? "write": "read");

  /* data given? */
  if (argc >= 4)
  {
    printf("access width given.\n");
    access_width = tolower(argv[3][0]);
  }
  printf("access width: ");
  if (access_width == 'w')
    printf("word (32-bits)\n");
  else
  {
    printf("word (32-bits)\n");
    access_width = 'w';
  }

    if ((fd = open(argv[1], O_RDWR | O_SYNC)) == -1) FATAL;
    printf("character device %s opened.\n", argv[1]); 
    fflush(stdout);

    /* map one page */
    map_base = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (map_base == (void *) -1) FATAL;
    printf("Memory mapped at address %p.\n", map_base); 
    fflush(stdout);

    /* calculate the virtual address to be accessed */
    virt_addr = map_base + target;
    /* read only */
    if (argc <= 4) {
      //printf("Read from address %p.\n", virt_addr); 
      switch(access_width) {
	case 'w':
    
	  read_result = *((uint32_t *) (virt_addr + 0x200));
    read_result = ltohl(read_result);
    //printf("Read 32-bit value at address 0x%08x (%p): 0x%08x\n", (unsigned int)target, virt_addr, (unsigned int)read_result);
    printf("DIVCLK_DIVIDE = %d \n", (read_result & 0x000000ff));
    printf("CLKFBOUT_MULT = %d.%d \n", (read_result & 0x0000ff00) >> 8, (read_result & 0x03ff0000) >> 16);
    cal_clk = cal_clk / (read_result & 0x000000ff);
    //printf("cal_clk = %f \n", cal_clk);
    cal_clk = cal_clk * (((read_result & 0x0000ff00) >> 8) + (float)((read_result & 0x03ff0000) >> 16) / 1000);
    //printf("cal_clk = %f \n", cal_clk);
	  read_result = *((uint32_t *) (virt_addr + 0x208));
    read_result = ltohl(read_result);
    //printf("Read 32-bit value at address 0x%08x (%p): 0x%08x\n", (unsigned int)target, virt_addr, (unsigned int)read_result);
    printf("CLKOUT0_DIVIDE = %d.%d \n", (read_result & 0x000000ff), (read_result & 0x0003ff00) >> 8);
    cal_clk = cal_clk / ((read_result & 0x000000ff) + (float)((read_result & 0x0003ff00) >> 8) / 1000);
    printf("Original Clock = %f \n", cal_clk);

    return (int)read_result;
	  break;
	default:
	  fprintf(stderr, "Illegal data type '%c'.\n", access_width);
	  exit(2);
      }
      fflush(stdout);
    }
    /* data value given, i.e. writing? */
    if (argc >= 5)
    {
      WNS = atof(argv[4]);
      switch (access_width)
      {
        case 'w':
          read_result = *((uint32_t *) (virt_addr + 0x200));
          read_result = ltohl(read_result);
          DIVCLK_DIVIDE = (float)(read_result & 0x000000ff);
          CLKFBOUT_MULT = (float)((read_result & 0x0000ff00) >> 8) + (float)((read_result & 0x03ff0000) >> 16) / 1000;
          
          read_result = *((uint32_t *) (virt_addr + 0x208));
          read_result = ltohl(read_result);
          CLKOUT0_DIVIDE = (float)(read_result & 0x000000ff) + (float)((read_result & 0x0003ff00) >> 8) / 1000;

          printf("DIVCLK_DIVIDE = %3f\n", DIVCLK_DIVIDE);
          printf("CLKFBOUT_MULT = %3f\n", CLKFBOUT_MULT);
          printf("CLKOUT0_DIVIDE = %3f\n", CLKOUT0_DIVIDE);
          cal_clk = cal_clk / DIVCLK_DIVIDE * CLKFBOUT_MULT / CLKOUT0_DIVIDE;
          printf("Original Clock = %3fMHz \n", cal_clk);
          original_period = 1000 / cal_clk;
          printf("Original Period = %3fns\n", original_period);
          printf("WNS = %3f\n", WNS);
          scaled_period = WNS + original_period;
          scaled_period = (int)(scaled_period * 1000) / 1000;

          printf("Scaled Period = %3fns\n", scaled_period);
          scaled_clk = 1000 / scaled_period;
          printf("Scaled Frequency = %dMHz\n", (int)scaled_clk);

          writeval = (int)scaled_clk;

          // Rule DIVCLK_DIVIDE = 1~106
          // Rule CLKFBOUT_MULT = (2.000~128.000) Fractional should be 0.125 unit
          // Rule CLKOUT0_DIVIDE = (1.000~128.000) Fractional should be 0.125 unit
          for(i = 2 ; i < 107 ; i++){
            for(k = 16 ; k < 1025 ; k++){
              for(j = 16 ; j < 1025 ; j++){
                temp_clk = 100 / i;
                temp_clk = temp_clk * j * 0.125;
                temp_clk = temp_clk / (k * 0.125);

                if(fabsf(temp_clk - writeval) < 0.01 && ((j*0.125) / i) >= 8  && ((j*0.125) / i) <= 16){
                  printf("%f\n", fabsf(temp_clk - writeval));
                  printf("first_break\n");
                  break;
                }
              }

              if(fabsf(temp_clk - writeval) < 0.01 && ((j*0.125) / i) >= 8  && ((j*0.125) / i) <= 16){
                break;
              }
            }
            if(fabsf(temp_clk - writeval) < 0.01 && ((j*0.125) / i) >= 8  && ((j*0.125) / i) <= 16){
              DIVCLK_DIVIDE = i;
              CLKFBOUT_MULT = j*0.125;
              CLKOUT0_DIVIDE = k*0.125;
              printf("temp_clk = %f\n",temp_clk);
              printf("writeval = %f\n", (float)writeval);
              printf("DIVCLK_DIVIDE = %d, CLKFBOUT_MULT = %f, CLKOUT0_DIVIDE = %f \n", (int)DIVCLK_DIVIDE, CLKFBOUT_MULT, CLKOUT0_DIVIDE);
              break;
            }
          }
          
          writeval = DIVCLK_DIVIDE;
          writeval = writeval + ((int)(CLKFBOUT_MULT) << 8);
          writeval = writeval + ((int)((int)(CLKFBOUT_MULT * 1000) % 1000) << 16);
          printf("writeval = %08x \n", writeval);
          writeval = htoll(writeval);
          *((uint32_t *) (virt_addr + 0x200)) = writeval; 
          writeval = (int)CLKOUT0_DIVIDE;
          writeval = writeval + ((int)(CLKOUT0_DIVIDE * 1000) % 1000 << 8);
          printf("writeval = %08x \n", writeval);
          writeval = htoll(writeval);
          *((uint32_t *) (virt_addr + 0x208)) = writeval; 

          writeval = 3;
          writeval = htoll(writeval);
          *((uint32_t *) (virt_addr + 0x25c)) = writeval;

          read_result = *((uint32_t *) (virt_addr + 0x25c));
          printf("status %d\n", read_result);
          while(read_result != 2){
            read_result = *((uint32_t *) (virt_addr + 0x25c));
          }
          printf("status %d\n", read_result);

          /* swap 32-bit endianess if host is not little-endian */
          //writeval = htoll(writeval);          
          //*((uint32_t *) virt_addr) = writeval;
#if 0
          if (argc > 4) {
            read_result = *((uint32_t *) virt_addr);
            printf("Written 0x%08x; readback 0x%08x\n", writeval, read_result); 
          }
#endif
	  break;
      }
      fflush(stdout);
    }
    if (munmap(map_base, MAP_SIZE) == -1) FATAL;
    close(fd);
    return 0;
}


