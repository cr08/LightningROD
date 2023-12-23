import json
import pathlib
import os
import auth
from auth import FordPassAuthenticator, FordPassChargeLogsDownloader, download_status
from influx import InfluxDBHandler
from config import influx_url, influx_org, influx_bucket, influx_token
from config import fordpass_username, fordpass_password, fordpass_vin, fordpass_region, veh_model, veh_year

cwd = os.path.dirname(os.path.abspath(__file__))

VIC_YEAR = veh_year
VIC_MODEL = veh_model


if __name__ == "__main__":
    lightningRDir = pathlib.Path(__file__).parent.resolve()
    authenticator = FordPassAuthenticator(fordpass_username, fordpass_password, fordpass_vin, fordpass_region)
    energyLogs = FordPassChargeLogsDownloader(authenticator)
    authenticator.auth()
    energyLogs.download_charge_logs()
    download_status()

    # influx_handler = InfluxDBHandler(
    #     url=influx_url,
    #     token=influx_token,
    #     org=influx_org,
    #     bucket=influx_bucket,
    # )

    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    if VIC_YEAR != "":
        VIC_YEAR = VIC_YEAR.replace(" ", "_") + "-"
    if VIC_MODEL != "":
        VIC_MODEL = VIC_MODEL.replace(" ", "_")
    else:
        VIC_MODEL = "my"

        clog_fileName = os.path.join(cwd, f"{VIC_YEAR}{VIC_MODEL}_chargelog_{current_datetime}{REDACTION_STATUS}.json")


    # lightningRLogs = os.path.join(lightningRDir, "charge_logs.json")

        with open(clog_fileName, 'r') as file:
            charge_logs = json.load(file)

    # influx_handler.write_charge_logs_to_influxdb(charge_logs)
    # influx_handler.close()
