from tuya_iot import TuyaOpenAPI

# Replace these with your Tuya Cloud project details
ACCESS_ID = "your_access_id"
ACCESS_SECRET = "your_access_secret"
API_ENDPOINT = "https://openapi.tuyaeu.com"  # Choose the correct endpoint for your region
USER_ID = "your_user_id"

# Initialize the TuyaOpenAPI client
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_SECRET)
openapi.connect()

# Example: Get a list of devices
def get_devices():
    response = openapi.get("/v1.0/users/{}/devices".format(USER_ID))
    return response

# Example: Control a device
def control_device(device_id, commands):
    response = openapi.post(
        f"/v1.0/devices/{device_id}/commands", {"commands": commands}
    )
    return response

import argparse

parser = argparse.ArgumentParser(description="Tuya API CLI Tool")
parser.add_argument("--list-devices", action="store_true", help="List all devices")
parser.add_argument("--control-device", nargs=2, metavar=("device_id", "command"), help="Control a device")
args = parser.parse_args()

if args.list_devices:
    devices = get_devices()
    print("Devices:", devices)

if args.control_device:
    device_id, command = args.control_device
    command_data = [{"code": "switch_1", "value": command.lower() == "on"}]
    result = control_device(device_id, command_data)
    print("Command Result:", result)

