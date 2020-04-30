from utils import utils as utils
import pyselenium

def myfunction():
    name=utils.currenttestname()
    print(name)


myfunction()