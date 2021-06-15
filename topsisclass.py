import numpy as np
from scipy.stats import rankdata
import warnings

class TOPSIS():

    degerlendirme_matrisi = np.array([])
    agirlikli_normalize = np.array([])
    normallesmis_kararmatrisi = np.array([])
    M = 0
    N = 0


    def __init__(self,degerlendirme_matrisi,agirlik_matrisi,kriter):

        self.degerlendirme_matrisi = np.array(degerlendirme_matrisi,dtype="float")

        self.satir = len(self.degerlendirme_matrisi)
        self.sutun = len(self.degerlendirme_matrisi[0])
        self.agirlik_matrisi = np.array(agirlik_matrisi,dtype="float")
        self.agirlik_matrisi = self.agirlik_matrisi / sum(self.agirlik_matrisi)
        self.kriter = np.array(kriter)

    def adim1(self):
        self.normallesmis_kararmatrisi = np.copy(self.degerlendirme_matrisi)
        karealma_sum = np.zeros(self.sutun)
        for i in range(self.satir):
            for j in range(self.sutun):
                karealma_sum[j] += self.degerlendirme_matrisi[i, j] ** 2
        for i in range(self.satir): #
            for j in range(self.sutun):
                self.normallesmis_kararmatrisi[i,j] = self.degerlendirme_matrisi[i,j] / (karealma_sum[j]**0.5)
    def adim2(self):
        from pdb import set_trace
        self.agirlikli_normalize =np.copy(self.normallesmis_kararmatrisi)
        for i in range(self.satir):
            for j in range(self.sutun):
                self.agirlikli_normalize[i,j] *= self.agirlik_matrisi[j]

    def adim3(self):
        self.negatifideal_alternatif = np.zeros(self.sutun)
        self.ideal_alternatif = np.zeros(self.sutun)

        for i in range(self.sutun):
            if self.kriter[i]:
                self.negatifideal_alternatif[i] = min(self.agirlikli_normalize[:,i])
                self.ideal_alternatif[i] = max(self.agirlikli_normalize[:,i])
            else:
                self.negatifideal_alternatif[i] = max(self.agirlikli_normalize[:,i])
                self.ideal_alternatif[i] = min(self.agirlikli_normalize[:,i])

    def adim4(self):
        self.siarti_mesafe = np.zeros(self.satir)
        self.sieksi_mesafe = np.zeros(self.satir)

        self.siarti_mesafe_islem = np.copy(self.agirlikli_normalize)
        self.sieksi_mesafe_islem = np.copy(self.agirlikli_normalize)

        for i in range(self.satir):
            for j in range(self.sutun):
                self.sieksi_mesafe_islem[i][j] = (self.agirlikli_normalize[i][j] - self.negatifideal_alternatif[j]) ** 2
                self.siarti_mesafe_islem[i][j] = (self.agirlikli_normalize[i][j] - self.ideal_alternatif[j]) ** 2

                self.sieksi_mesafe[i] += self.sieksi_mesafe_islem[i][j]
                self.siarti_mesafe[i] += self.siarti_mesafe_islem[i][j]

        for i in range(self.satir):
            self.sieksi_mesafe[i] = self.sieksi_mesafe[i] ** 0.5
            self.siarti_mesafe[i] = self.siarti_mesafe[i] ** 0.5

    def adim5 (self):
        np.seterr(all = 'ignore')
        self.x1 = np.zeros(self.satir)
        self.x2 = np.zeros(self.satir)

        for i in range(self.satir):
            self.x1[i] = self.sieksi_mesafe[i] / (self.sieksi_mesafe[i] + self.siarti_mesafe[i])
            self.x2[i] = self.siarti_mesafe[i] / (self.sieksi_mesafe[i] + self.siarti_mesafe[i])

    def alternatifsiralamasi(self):

        return rankdata(self.x2, method='min').astype(int)


    def hesaplama(self):
        self.adim1()
        self.adim2()
        self.adim3()
        self.adim4()
        self.adim5()
