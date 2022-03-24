#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(.gnu.linkonce.this_module) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section(__versions) = {
	{ 0xf654425, "module_layout" },
	{ 0x2d3385d3, "system_wq" },
	{ 0x27e84c6c, "dma_direct_unmap_sg" },
	{ 0x5c36ab10, "device_remove_file" },
	{ 0x2933c44e, "cdev_del" },
	{ 0xaa279e7c, "kmalloc_caches" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0x991e89dc, "cdev_init" },
	{ 0xf888ca21, "sg_init_table" },
	{ 0x84548cc6, "put_devmap_managed_page" },
	{ 0x2fae8324, "pci_read_config_byte" },
	{ 0x46cf10eb, "cachemode2protval" },
	{ 0x3fd78f3b, "register_chrdev_region" },
	{ 0x808bf5d3, "dma_set_mask" },
	{ 0x5367b4b4, "boot_cpu_data" },
	{ 0x6eb78b88, "pci_disable_device" },
	{ 0x2e2165da, "pci_disable_msix" },
	{ 0x837b7b09, "__dynamic_pr_debug" },
	{ 0x77f3e1e5, "device_destroy" },
	{ 0x3afb11a7, "kobject_set_name" },
	{ 0x6729d3df, "__get_user_4" },
	{ 0xc7a9c532, "pci_release_regions" },
	{ 0xf5a94f16, "pcie_capability_clear_and_set_word" },
	{ 0x6091b333, "unregister_chrdev_region" },
	{ 0x999e8297, "vfree" },
	{ 0xa8096956, "dma_free_attrs" },
	{ 0x7a2af7b4, "cpu_number" },
	{ 0x97651e6c, "vmemmap_base" },
	{ 0x3c75f900, "pv_ops" },
	{ 0xcddef21, "dma_set_coherent_mask" },
	{ 0x15ba50a6, "jiffies" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0xb44ad4b3, "_copy_to_user" },
	{ 0x1f499541, "pci_set_master" },
	{ 0x976fb98e, "pci_iounmap" },
	{ 0x3812050a, "_raw_spin_unlock_irqrestore" },
	{ 0xc5850110, "printk" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0x131f7919, "dma_alloc_attrs" },
	{ 0x633e2cb3, "device_create" },
	{ 0x2072ee9b, "request_threaded_irq" },
	{ 0x31cb76d8, "pci_enable_msi" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0xe15d3b5c, "pci_find_capability" },
	{ 0x5ac43d5b, "device_create_file" },
	{ 0x86e95978, "cdev_add" },
	{ 0xb2fd5ceb, "__put_user_4" },
	{ 0x450fa832, "pci_enable_msix_range" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0x1000e51, "schedule" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0xa0b04675, "vmalloc_32" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0xc7ffe0ca, "pci_unregister_driver" },
	{ 0x5362bb62, "kmem_cache_alloc_trace" },
	{ 0xdbf17652, "_raw_spin_lock" },
	{ 0x51760917, "_raw_spin_lock_irqsave" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x37a0cba, "kfree" },
	{ 0xa698520c, "dma_direct_map_sg" },
	{ 0xe9b538e, "remap_pfn_range" },
	{ 0xf7f5becf, "pci_request_regions" },
	{ 0x42d93644, "pci_disable_msi" },
	{ 0x516eeec1, "__pci_register_driver" },
	{ 0x67521b43, "class_destroy" },
	{ 0x92540fbf, "finish_wait" },
	{ 0xc5b6f236, "queue_work_on" },
	{ 0x656e4a6e, "snprintf" },
	{ 0x985d41e4, "pci_iomap" },
	{ 0xd39dae27, "vmalloc_to_page" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x7c049318, "pci_enable_device" },
	{ 0x362ef408, "_copy_from_user" },
	{ 0xeccabe2b, "param_ops_uint" },
	{ 0x26ec0919, "__class_create" },
	{ 0x61443fb8, "dma_ops" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x4c849df5, "__put_page" },
	{ 0xe484e35f, "ioread32" },
	{ 0x47e60e80, "get_user_pages_fast" },
	{ 0xd1bd127f, "pcie_capability_read_word" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x587f22d7, "devmap_managed_key" },
	{ 0x8a35b432, "sme_me_mask" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v000010EEd0000D020sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00005020sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00005021sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009011sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009012sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009014sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009018sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd0000901Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009021sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009022sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009024sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009028sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd0000902Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009031sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009032sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009034sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00009038sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd0000903Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008011sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008012sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008014sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008018sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008021sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008022sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008024sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008028sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008031sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008032sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008034sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00008038sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007011sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007012sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007014sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007018sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007021sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007022sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007024sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007028sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007031sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007032sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007034sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v000010EEd00007038sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "F768050AD316E4722617616");
