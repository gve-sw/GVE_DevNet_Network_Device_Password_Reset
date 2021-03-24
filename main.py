""" Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from netmiko import ConnectHandler
import csv

# reading csv file that contains the hostname, user, and password
with open("creds.csv") as f:
    reader = csv.reader(f,delimiter=",")
    next(reader,None)
    data_read = [row for row in reader]

password = input("Choose new password : ")
r = input("press e to continue with the password change : ")

if r.lower() == "e":
    
    for data in data_read:

        device = {
            "ip":data[0],
            "username":data[1],
            "password":data[2],
            "device_type":"cisco_ios"
            }
        try:
            net_connect = ConnectHandler(**device)
        except:
            error_text = "unable to connnect to " + data[0] + " check credentials"
            print(error_text)

            file_obj = open("error.txt","a")
            file_obj.write(error_text)
            file_obj.close

            continue

        # updating enable password
        net_connect.send_config_set(["enable password " + password])

        # updating enable secret
        net_connect.send_config_set(["enable secret " + password])

        # updating line console password
        net_connect.send_config_set(["line con 0","password " + password])

        # updating VTY lines
        net_connect.send_config_set(["line vty 0 4","password " + password])


        # gathering list of users on the device
        response = net_connect.send_command("sh run | i user")
        file_obj = open("response.txt","w")
        file_obj.write(response)
        file_obj.close

        file_obj = open("response.txt","r")
        Lines = file_obj.readlines()
        count = 0
        users = []

        for line in Lines:
            user = {}
            count += 1
            text = line.strip()
            text = text.split(" ")
            user["user"] = text[1]
            user["priv"] = text[3]
            users.append(user)

        for user in users:
            # change each user's secret
            net_connect.send_config_set(["username " + user["user"] + " privilege " + user["priv"] + " secret " + password])

        file_obj = open("log.txt","a")
        file_obj.write("Device " + data[0] + " has had the passwords reset to " + password)
        file_obj.close
    

else:
    print("shutting off")