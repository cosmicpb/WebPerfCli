# WebPerfCli
## Extract Web Vitals data with command line (Python/CLI).

WebPerfCli is a web performance CLI application to measure Web Vitals without html tags inside your code.

Just running a easy command in python terminal and you be able to see the metrics of your test.

## Features

- Import a .CSV file with all the URLs to be tested
- You can choose between Desktop and Mobile environments
- Export a .CSV file as output

## Installation

WebPerfCli

Download the code:

```sh
git clone https://github.com/cosmicpb/WebPerfCli.git

```

Install dependencies:

```sh
cd WebPerfCli
pip install -r requirements.txt
```

## Using the WebPerfCli

1. Set the data mass: Open massa.csv file and add the URLs that need to be tested.
2. Open the [PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/get-started) page and get an API Key.
3. Run the command below:

```sh
python webperf.py -d massa.csv -s desktop -k <YOUR_KEY> -o output.csv
```

## Output
O arquivo output.csv é gravado na seguinte ordem:

dd_mm_YYYY.HH_MM_SS, URL, Status Code, LCP, CLS, TBT.

## License
MIT

Developed by Paulo Baldacim Junior

**Free Software, Hell Yeah!**


