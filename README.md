# Safer

Safer is a RESTful API written in Python using Flask which is mount it inside a docker container and accessible via Tor. Each file is encrypted itself and can be only decrypted using a **Key**; this key is generated using a *password*. In order download the file you will need the *ID* of the file and the *Key*. Since the key isn't stored by the API will need to save it by yourself. The funny thing is that a [Hidden Service](https://2019.www.torproject.org/docs/onion-services) is created and an **.onion v3** is generated.

## Installation

First, we need **Docker Compose**. Please refer to the official documentation [here](https://docs.docker.com/compose/install/). After installing **Docker Compose**, clone this repo and move into the `safer` folder:

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

## Thanks

[Christophe Mehay](https://github.com/cmehay) because his amazon work on [goldy/tor-hidden-service/](https://hub.docker.com/r/goldy/tor-hidden-service/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
