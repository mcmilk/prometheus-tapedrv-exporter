
# Prometheus Tapedrive Exporter

A small shell script for gathering metrics from tape drives inside libraries such as the [IBM TS4500](https://www.ibm.com/products/ts4500).
The collected information can be used by [Prometheus](https://prometheus.io/) for monitoring and alerting.

## Features

- Queries tape drives within supported libraries
  - currently these tape drives should work:
    - Ultrium 3-SCSI .. Ultrium 9-SCSI
    - ULT3580-TD3 .. ULT3580-TD9
- Exports basic health and status information
- Simple to integrate with Prometheus node exporters

## Contributors

- Tino Reichardt ([Deutsches Elektronen-Synchrotron DESY](https://www.desy.de/))

## Installation

Clone this repository and place the script and the systemd unit into the
right places.

```bash
git clone https://github.com/mcmilk/prometheus-tapedrv-exporter.git
cp usr/lib/systemd/system/tapedrv-exporter.service /usr/lib/systemd/system
cp usr/sbin/tapedrv-exporter-daemon /usr/sbin
systemctl enable tapedrv-exporter
systemctl start tapedrv-exporter
```

Run `tapedrv-exporter-daemon getinfo` to preview the exported information.

## Contributing

Contributions are welcome!
Each submitted patch must include a Signed-off-by line.
Patches without this line will not be accepted.
