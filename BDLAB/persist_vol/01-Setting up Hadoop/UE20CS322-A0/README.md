# Virtual Machine Setup - Assignment 0

The purpose of this assignment is to setup a virtual machine for the course with the required specifications. Dual booting is discouraged since the tools we would be using could cause issues with the entire system. This assignment is not graded. This is only a guideline for the setup for future assignments.

In every place where an SRN is present, replace it with your SRN **IN LOWER CASE**. This is very important since all auto-evaluations of hands-on tutorials will be based on that.

Contents:

1. [Downloads](#step1)
2. [Virtual Machine Provisioning](#step2)
3. [VM Configuration](#step3)
   * [VMWare Workstation Player](#step3a)
   * [Oracle VirtualBox](#step3b)
4. [Virtual Machine Boot-up](#step4)
5. [Installation Verification](#step5)

## <a name="step1"></a> Step 1 - Downloads

Download a Virtual Machine hypervisor. You are free to choose any of the following options. However, it is recommended that you use VMWare Workstation Player.

- [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [VMWare Workstation Player](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html)

Download the latest Ubuntu image, that is 22.04. **20.04 OR ANYTHING LOWER IS NOT ACCEPTED.** Link to the image is [here](https://ubuntu.com/download/desktop).

## <a name="step2"></a> Step 2 - Virtual Machine Provisioning

Minimum specifications for the virtual machine:

- 2 processors.
- 4GB memory.
- 30GB storage/HDD space.
- OS Image : Ubuntu 22.04

Recommended specifications:

- Half the processors available.
- 8GB memory or half the memory available.
- 50GB storage/SSD space.

## <a name="step3"></a> Step 3 - VM Configuration

### <a name="step3a"></a> Step 3a - for VMWare Workstation Player users

Enable for non-commercial use.

![Non-commercial use](https://cdn.discordapp.com/attachments/1001143746664091698/1003979018107879475/unknown.png)

The full name and username of the VM should be your SRN in lowercase as shown in the pic.

![naming](https://cdn.discordapp.com/attachments/1001143746664091698/1001143979875782718/unknown.png)

Your virtual machine name should also be your SRN in lowercase.

![vnaming](https://cdn.discordapp.com/attachments/1001143746664091698/1004050627418149004/unknown.png)

Provide 30GB (or more, check recommended specs) of storage space and split it into multiple disks.

![storage](https://cdn.discordapp.com/attachments/1001143746664091698/1004042045788270772/unknown.png)

Head over to "Customize Hardware". Provide at least 4GB of memory and 2 processors. Refer to recommended specifications above for better performance.

![4ram](https://cdn.discordapp.com/attachments/1001143746664091698/1004042925329612910/unknown.png)
![2proc](https://media.discordapp.net/attachments/1001143746664091698/1004043084675436664/unknown.png)

Your final configuration should resemble the image given below.

![final](https://cdn.discordapp.com/attachments/1001143746664091698/1004077410150535278/unknown.png)

### <a name="step3b"></a> Step 3b - for VirtualBox users

Name your OS with your SRN in lowercase

![srnname](https://cdn.discordapp.com/attachments/1001143746664091698/1003658070964048052/unknown.png)

Provide at least 4GB of memory.

![4ram](https://cdn.discordapp.com/attachments/1001143746664091698/1003658148776783932/unknown.png)

Create a new VMDK hard-disk of fixed size and at least 30GB of storage space.

![createnew](https://cdn.discordapp.com/attachments/1001143746664091698/1003658274354245682/unknown.png)

![vmdk](https://cdn.discordapp.com/attachments/1001143746664091698/1003658396291051520/unknown.png)

![fixedsize](https://cdn.discordapp.com/attachments/1001143746664091698/1003658481624158278/unknown.png)

![30gb](https://cdn.discordapp.com/attachments/1001143746664091698/1003658536817016952/unknown.png)

Once the VM is created, head over to Settings -> System -> Processor. Provide at least 2 processors and 100% execution cap.

![2proc](https://cdn.discordapp.com/attachments/1001143746664091698/1003660323015905352/unknown.png)

Then under Settings -> Storage, choose the OS image you want to use.

![iso](https://cdn.discordapp.com/attachments/1001143746664091698/1003661073175543871/unknown.png)

## <a name="step4"></a> Step 4 - Virtual Machine Boot-up

The initial boot-up might take up to 90 minutes. During this, a few more fields have to be filled.

Do not worry about this pop-up:

![erasedisk](https://cdn.discordapp.com/attachments/1001143746664091698/1004047835995582504/unknown.png)

This just means that the virtual machine disk created does not have any OS on it. Your host storage will not be affected.

Irrespective of whether you are using VMWare or VirtualBox, you need to provide your SRN in lowercase in "Your computer's name" and "Pick a username".

![srn](https://cdn.discordapp.com/attachments/1001143746664091698/1003663857933373460/unknown.png)

Other configuration choices are up to you.

At the end of the boot-up, head over to the terminal and type the following command:

```sh
sudo apt-get update -y
sudo apt-get upgrade -y
```

## <a name="step5"></a> Step 5 - Installation Verification

To verify that the installation went well, head over to the terminal and type the following command:

```sh
# Clone the repository first
git clone https://github.com/Cloud-Computing-Big-Data/UE20CS322-A0.git
cd UE20CS322-A0
python3 verify-installation.pyc
```
