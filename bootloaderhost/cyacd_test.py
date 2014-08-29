from cStringIO import StringIO
import unittest

import cyacd


class BootloaderRowTest(unittest.TestCase):
	def testParseRow(self):
		rowdata = ":000018008000100020110C0000E92D0000E92D000008B5024B83F3088802F0E8F800100020F8B572B6002406236343704D0134EE187279707831793778B3781202F67800020A4338431904084337063843002103F09FF8032CE7D1291C12316548802203F08EF80023191C634AFF25141C143418593C32061CAE434F00C4B2351CD219002CB8"
		blrow = cyacd.BootloaderRow.read(rowdata)
		self.assertEquals(blrow.array_id, 0)
		self.assertEquals(blrow.row_number, 0x18)
		self.assertEquals(len(blrow.data), 0x80)
		self.assertEquals(blrow.data.encode('hex').upper(), rowdata[11:-2])

	def testParseFile(self):
		filedata = """04A611931101
:000018008000100020110C0000E92D0000E92D000008B5024B83F3088802F0E8F800100020F8B572B6002406236343704D0134EE187279707831793778B3781202F67800020A4338431904084337063843002103F09FF8032CE7D1291C12316548802203F08EF80023191C634AFF25141C143418593C32061CAE434F00C4B2351CD219002CB8
:000019008007D0167857787619013C3770E4B20232F5E7C0B204330918282BE4D1564A574B574C584D584F59491A6099262C604F20574A584B584D3E600F240860574F58491A6003262C608720564B574C3E603C220860564DD82756491A6038012260554A2E60554B0860554C554D56481660C0270E2655491E6002222C6093260760534BB3"""
		bldata = cyacd.BootloaderData.read(StringIO(filedata))
		self.assertEquals(bldata.silicon_id, 0x04A61193)
		self.assertEquals(bldata.silicon_rev, 0x11)
		self.assertEquals(bldata.checksum_type, 0x01)
		self.assertEquals(len(bldata.rows), 2)
		self.assertTrue(all(isinstance(row, cyacd.BootloaderRow) for row in bldata.rows))


if __name__ == '__main__':
	unittest.main()