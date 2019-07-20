# Safer

Safer is a torifyed dockerized **RESTful API** for storing encrypted files.

## Installation

First, we need **Docker Compose**. Please refer to the official documentation [here](https://docs.docker.com/compose/install/).

After installing Docker, clone this repo and move into the `safer` folder:

```bash
$ git clone https://github.com/davidtavarez/safer.git
$ cd safer
```

Now, we just need to run the manage script

```bash
$ bash manage
```
```
  _____  ____  _____  ___  ____
 / ___/ /    ||     |/  _]|    \
(   \_ |  o  ||   __/  [_ |  D  )
 \__  ||     ||  |_|    _]|    /
 /  \ ||  _  ||   _]   [_ |    \
 \    ||  |  ||  | |     ||  .  \
  \___||__|__||__| |_____||__|\_|
------------------------------------------------------------------------
Usage: manage [-h]
Usage: manage [option...] --{init|start|halt|clean|stats}

   --- MANAGEMENT ---
   -i, --init, init           Initializes the development environment.
   -s, --start, start         Starts all configured services.
   -p, --halt, halt           Stops all configured services.
   -r, --relaod, reload       Restart all configured services.
   -b, --rebuild, rebuild     Rebuild all configured services.
   -c, --clean, clean         Cleans containers, volumes, images.

   --- UTILITIES ---
   -o, --onion, onion         Get the onion URL.
   -h, --help, help           Shows this help box.
------------------------------------------------------------------------

```

Great! we're ready to go!

## Usage

Uploading files:

```bash
$ upload /PATH/TO/FILE.EXT PASSWORD
{"id": 1, "key": "QRhtN5X4oGR8GxlLSEL1GJJlZgf64VXyMkx7YIbvVK4="}
```

Downloading files:

```bash
$ download 1 "QRhtN5X4oGR8GxlLSEL1GJJlZgf64VXyMkx7YIbvVK4\=" FILE.EXT
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
