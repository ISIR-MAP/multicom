""" Test module for com.py """
import unittest
import time
import com
import random
import sys
class TestFonctionDevice(unittest.TestCase):
    """ Device functions tests """
    def setUp(self):
        self.hapticd = com.HDevice("ftdi")
    def test_extract(self):
        """ Test extract function """
        size = 5
        for i in range(0, size):
            self.hapticd.fifoin.put(bytes([i]))
        fifoverif = bytearray(range(0, size))
        fifotest = self.hapticd.extract(size)
        self.assertEqual(fifotest, fifoverif)
    def test_get(self):
        """Test get function"""
        var = "toto"
        self.hapticd.fifoin.put(var)
        self.assertEqual(self.hapticd.get(), var)
    def test_readarray(self):
        """ Test readarray function """
        size = 5
        for i in range(0, size):
            self.hapticd.fifoin.put(bytes([i]))
        fifoverif = bytearray(range(0, size))
        fifotest = self.hapticd.readarray(size)
        self.assertEqual(fifotest, fifoverif)
    def test_incommingsize(self):
        """Test size"""
        size = 5
        for i in range(0, size):
            self.hapticd.fifoin.put(bytes([i]))
        time.sleep(0.1)
        sizecomp = self.hapticd.incommingsize()
        self.assertEqual(size, sizecomp)
    def test_writeint(self):
        """ test conversion byte """
        tosend = 45
        bufenvoi = bytearray(4)
        bufenvoi[0] = int(tosend) & int('0b00111111', 2)
        bufenvoi[1] = ((int(tosend) >> 6) & int('0b00111111', 2)) | int('0b01000000', 2)
        bufenvoi[2] = ((int(tosend) >> 12) & int('0b00111111', 2)) | int('0b10000000', 2)
        bufenvoi[3] = int('0b11000000', 2)
        self.hapticd.writeint(tosend)
        self.assertEqual(bufenvoi, self.hapticd.fifoout.get())
    def testwrite(self):
        """ Test write """
        tosend = 45
        forcenow = max(min(tosend, 130), -130)
        forcenowint = 32767*(1+forcenow/130)
        bufenvoi = bytearray(4)
        bufenvoi[0] = int(forcenowint) & int('0b00111111', 2)
        bufenvoi[1] = ((int(forcenowint) >> 6) & int('0b00111111', 2)) | int('0b01000000', 2)
        bufenvoi[2] = ((int(forcenowint) >> 12) & int('0b00111111', 2)) | int('0b10000000', 2)
        bufenvoi[3] = int('0b11000000', 2)
        self.hapticd.write(tosend)
        self.assertEqual(bufenvoi, self.hapticd.fifoout.get())
    def teststartstop(self):
        """ Launch and quit """
        self.hapticd.launch()
        time.sleep(1)
        self.hapticd.quit()

class TestFonctionDeviceSerial(unittest.TestCase):
    """ Device functions tests """
    def setUp(self):
        self.hapticd = com.HDevice("com8")
    def test_extract(self):
        """ Test extract function """
        size = 5
        for i in range(0, size):
            self.hapticd.fifoin.put(bytes([i]))
        fifoverif = bytearray(range(0, size))
        fifotest = self.hapticd.extract(size)
        self.assertEqual(fifotest, fifoverif)
    def test_get(self):
        """Test get function"""
        var = "toto"
        self.hapticd.fifoin.put(var)
        self.assertEqual(self.hapticd.get(), var)
    def test_readascii(self):
        """Test readascii"""
        var = "toto"
        self.hapticd.fifoin.put(var.encode('ascii', 'backslashreplace'))
        self.assertEqual(self.hapticd.readascii(), var)
    def test_readsep(self):
        """Test read with separateur"""
        size = 8
        var = ""
        result = []
        for i in range(0, size):
            result.append(random.uniform(0, 50))
            var = var + str(result[i]) + "|"
        self.hapticd.fifoin.put(var.encode('ascii', 'backslashreplace'))
        retour = self.hapticd.readsep(r"\|", size)[0]
        for i in range(0, size):
            self.assertEqual(float(retour[i]), result[i])
    def teststartstop(self):
        """ Launch and quit """
        self.hapticd.launch()
        time.sleep(1)
        self.hapticd.quit()
if __name__ == '__main__':
    unittest.main()
