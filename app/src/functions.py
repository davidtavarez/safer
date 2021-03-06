# coding=utf-8

import base64
import os
import random
import time
import string

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from werkzeug.utils import secure_filename


def get_filename(file_path: str) -> str:
    head, file_name = os.path.split(file_path)
    return file_name


def generate_key(password: str, salt: bytes) -> str:
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def encrypt(data, key) -> bytes:
    return Fernet(key).encrypt(base64.b64encode(data))


def decrypt(data, key) -> bytes:
    return base64.b64decode(Fernet(key).decrypt(data))


def create_encrypted_file(filename: str, content, key, base_path: str) -> str:
    filename = secure_filename(filename)
    folder = os.path.join(base_path, str(time.time()))
    os.makedirs(folder)
    file_path = os.path.join(folder, filename)

    encrypted_content = encrypt(content, key)

    with open(file_path, "wb") as f:
        f.write(encrypted_content)
        f.close()

    return file_path


def decrypt_file(file_path: str, key) -> bytes:
    with open(file_path, 'rb') as f:
        data = f.read()
    return decrypt(data, key)


def get_random_bad_joke() -> str:
    bad_jokes = [
        "There are only 10 types of people in the world: those that understand binary and those that don't.",
        "Computers make very fast, very accurate mistakes.",
        "Be nice to the nerds, for all you know they might be the next Bill Gates!",
        "Artificial intelligence usually beats real stupidity.",
        "To err is human - and to blame it on a computer is even more so.",
        "CAPS LOCK – Preventing Login Since 1980.",
        "The truth is out there. Anybody got the URL?",
        "The Internet: where men are men, women are men, and children are FBI agents.",
        "Some things Man was never meant to know. For everything else, there’s Google.",
        "The box said \"Requires Windows Vista or better\". So I installed LINUX.",
        "UNIX is basically a simple operating system, but you have to be a genius to understand the simplicity.",
        "In a world without fences and walls, who needs Gates and Windows?",
        "C://dos && C://dos.run && run.dos.run",
        "Bugs come in through open Windows.",
        "Penguins love cold, they wont survive the sun.",
        "Unix is user friendly. It’s just selective about who its friends are.",
        "Failure is not an option. It comes bundled with your Microsoft product.",
        "NT is the only OS that has caused me to beat a piece of hardware to death with my bare hands.",
        "My daily Unix command list: unzip; strip; touch; finger; mount; fsck; more; yes; unmount; sleep.",
        "Microsoft: \"You've got questions. We've got dancing paperclips.\"",
        "Erik Naggum: \"Microsoft is not the answer. Microsoft is the question. NO is the answer.\"",
        "Windows isn’t a virus, viruses do something.",
        "Computers are like air conditioners: they stop working when you open Windows.",
        "Mac users swear by their Mac, PC users swear at their PC.",
        "If at first you don’t succeed; call it version 1.0.",
        "My software never has bugs. It just develops random features.",
        "I would love to change the world, but they won’t give me the source code.",
        "The code that is the hardest to debug is the code that you know cannot possibly be wrong.",
        "Beware of programmers that carry screwdrivers.",
        "Programming today is a race between software engineers striving to build bigger and better idiot-proof "
        "programs, and the Universe trying to produce bigger and better idiots.So far, the Universe is winning.",
        "The beginning of the programmer's wisdom is understanding the difference between getting program to run and "
        "having a runnable program.",
        "I'm not anti-social; I'm just not user friendly.",
        "Hey! It compiles! Ship it!",
        "If Ruby is not and Perl is the answer, you don't understand the question.",
        "The more I C, the less I see.",
        "COBOL programmers understand why women hate periods.",
        "Michael Sinz: \"Programming is like sex, one mistake and you have to support it for the rest of your life.",
        "If you give someone a program, you will frustrate them for a day; if you teach them how to program, you will "
        "frustrate them for a lifetime.\"",
        "Programmers are tools for converting caffeine into code.",
        "My attitude isn't bad. It's in beta.",
        "Enter any 11-digit prime number to continue.",
        "E-mail returned to sender, insufficient voltage.",
        "All wiyht. Rho sritched mg kegtops awound?",
        "Black holes are where God divided by zero.",
        "If I wanted a warm fuzzy feeling, I'd anti-alias my graphics!",
        "If brute force doesn't solve your problems, then you aren't using enough.",
        "SUPERCOMPUTER: what it sounded like before you bought it.",
        "Evolution is God's way of issuing upgrades.",
        "Linus Torvalds: \"Real men don’t use backups, they post their stuff on a public ftp server and let the rest "
        "of the world make copies.\"",
        "Hacking is like sex... you get in, you get out, and hope that you didn't leave something that can be traced "
        "back to you.",
        "There are three kinds of people: those who can count and those who can't.",
        "Latest survey shows that 3 out of 4 people make up 75% of the world’s population.",
        "Hand over the calculator, friends don’t let friends derive drunk.",
        "An infinite crowd of mathematicians enters a bar. The first one orders a pint, the second one a half pint, "
        "the third one a quarter pint... \"I understand\", says the bartender – and pours two pints.",
        "1f u c4n r34d th1s u r34lly n33d t0 g37 l41d.",
    ]

    return random.choice(bad_jokes)


def generate_random_string(min_char: int = 4, max_char: int = 6) -> str:
    all_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(all_characters) for x in range(random.randint(min_char, max_char)))
