import os
import traceback
import threading
from ftplib import FTP
from datetime import datetime
class Downloader:
    RR_DB_FTP = {}
    RR_DB_FTP['ripe_asnames']={'site':'ftp.ripe.net','path':'/ripe/asnames/','filename':'asn.txt','local_dir':'/home/Domeye/data/rir/'}
    RR_DB_FTP['apnic_aut_num'] = {'site':'ftp.apnic.net','path':'/apnic/whois/','filename':'apnic.db.aut-num.gz','local_dir':'./apnic'}
    RR_DB_FTP['apnic_route'] = {'site':'ftp.apnic.net','path':'/apnic/whois/','filename':'apnic.db.route.gz','local_dir':'./apnic'}
    RR_DB_FTP['apnic_route6'] = {'site':'ftp.apnic.net','path':'/apnic/whois/','filename':'apnic.db.route6.gz','local_dir':'./apnic'}
    RR_DB_FTP['apnic_inetnum'] = {'site': 'ftp.apnic.net', 'path': '/apnic/whois/', 'filename': 'apnic.db.inetnum.gz','local_dir': './apnic'}
    RR_DB_FTP['apnic_inet6num'] = {'site': 'ftp.apnic.net', 'path': '/apnic/whois/', 'filename': 'apnic.db.inet6num.gz','local_dir': './apnic'}
    RR_DB_FTP['ripe'] = {'site':'ftp.ripe.net','path':'/ripe/dbase/split/','filename':'ripe.db.aut-num.gz','local_dir':'./ripe/'}
    RR_DB_FTP['ripe_route'] = {'site':'ftp.ripe.net','path':'/ripe/dbase/split/','filename':'ripe.db.route.gz','local_dir':'./ripe/'}
    RR_DB_FTP['ripe_route6'] = {'site':'ftp.ripe.net','path':'/ripe/dbase/split/','filename':'ripe.db.route6.gz','local_dir':'./ripe/'}
    RR_DB_FTP['ripe_inetnum'] = {'site': 'ftp.ripe.net', 'path': '/ripe/dbase/split/', 'filename': 'ripe.db.inetnum.gz','local_dir': './ripe/'}
    RR_DB_FTP['ripe_inet6num'] = {'site': 'ftp.ripe.net', 'path': '/ripe/dbase/split/', 'filename': 'ripe.db.inet6num.gz','local_dir': './ripe/'}
    # RR_DB_FTP['radb_num'] = {'site':'ftp.radb.net','path':'/radb/dbase','filename':'radb.db.gz','local_dir':'./radb/%s'}
    RR_DB_FTP['afrinic'] = {'site':'ftp.afrinic.net','path':'/pub/dbase/','filename':'afrinic.db.gz','local_dir':'./afrinic'}
    RR_DB_FTP['arin'] = {'site':'ftp.arin.net','path':'/pub/rr/','filename':'arin.db.gz','local_dir':'./arin'}
    RR_DB_FTP['lacnic'] = {'site':'ftp.lacnic.net','path':'/lacnic/dbase/','filename':'lacnic.db.gz','local_dir':'./lacnic'}
    #下载数据
    def downLoad(self,source):
        date = datetime.now().strftime('%Y-%m-%d')
        print(date)
        localDir = self.RR_DB_FTP[source]['local_dir']+date
        print(localDir)
        #localDir = 'data'
        if (not os.path.exists(localDir)):
            os.makedirs(localDir)

        try:
            print("Downloading %s..." % source)
            ftp = FTP(self.RR_DB_FTP[source]['site'])
            ftp.login()
            ftp.cwd(self.RR_DB_FTP[source]['path'])
            ftp.retrbinary("RETR %s" % self.RR_DB_FTP[source]['filename'],
                           open("%s/%s" % (localDir, self.RR_DB_FTP[source]['filename']), 'wb').write)
            ftp.quit()
            print("Done downloading %s" % source)

        except:
            print("Error processing %s, skipping" % source)
            traceback.print_stack()

if __name__ == '__main__':
#     # downLoad('lacnic')
    downloader = Downloader()
    downloader.downLoad('ripe_asnames')
    #for source in downloader.RR_DB_FTP:
     #   t = threading.Thread(target=downloader.downLoad,args=(source,))
      #  t.start()
