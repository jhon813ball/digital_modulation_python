import numpy as np

class CommPath:
    
    def __init__(self):
        self.L = 0
        
    def awgn(self, x, snr_db):
        L = x.size
        snr_true = 10.0**(snr_db/10.0)
        Esym = sum(np.abs(x)**(2))/L
        N0 = Esym/snr_true
        if isinstance(x, complex):
            noiseSigma = np.sqrt(N0/2.0)
            n = noiseSigma*(np.random.randn(L)+1j*np.random.randn(L))
        else:
            noiseSigma = np.sqrt(N0)
            n = noiseSigma*np.random.randn(L)
        y = x + n
        return y
    
