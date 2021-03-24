# GVE_DevNet_Network_Device_Password_Reset
prototype code that allows the user to change the password to different lines from a network device (Cisco IOS)

The script will change 

- Cosole secret
- All user passwords within that device
- VTY line 0 4 password
- Enable secret
- Enable password


## Contacts
* Jorge Banegas

## Solution Components
* netmiko
* python

## Installation/Configuration

1. First step will be to include you the hostname,username, and password inside the config.csv file for the script to use

```csv
   hostname,username,password
   x.x.x.x,cisco,cisco
   x.x.x.x,cisco,cisco
```
2. Create virtual environment and name it env, then activate it

```console
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
```

4. Install the dependencies required for the python script
```console
foo@bar(env):~$ pip install -r requirements.txt
```

## Usage

To launch script:


    ```console
    foo@bar(env):~$ python main.py
    ```


# Screenshots

We will show the current password configuration of a virtual IOS router in Cisco Modeling Labs. 

![/IMAGES/before_script1.png](/IMAGES/before_script1.png)

![/IMAGES/before_script1.png](/IMAGES/before_script2.png)

![/IMAGES/before_script1.png](/IMAGES/before_script3.png)

Once the script is launched, it will ask the user the new password to use 

![/IMAGES/before_script1.png](/IMAGES/step1.png)

Will ask for confirmation with the password changes

![/IMAGES/before_script1.png](/IMAGES/step2.png)

After the execution of the password changes, script will log the action in the log.txt file. If there is a device that was not able to connect via SSH, it will be reported in the error.txt file.

![/IMAGES/before_script1.png](/IMAGES/log.png)

Now lets check back to the configurations to see if the passwords have been updated. You can see the secret hashes are now different as well.

![/IMAGES/before_script1.png](/IMAGES/after_script1.png)

![/IMAGES/before_script1.png](/IMAGES/after_script2.png)

![/IMAGES/before_script1.png](/IMAGES/after_script3.png)



![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
