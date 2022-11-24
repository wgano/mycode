class Solution:
    def romanToInt(self, s: str) -> int:
        n = str(s)
        iv = n.count('IV')
        ix = n.count('IX')
        xl = n.count('XL')
        xc = n.count('XC')
        cd = n.count('CD')
        cm = n.count('CM')
        i = n.count('I')-iv-ix
        v = n.count('V')-iv
        x = n.count('X')-xl-ix-xc
        l = n.count('L')-xl
        c = n.count('C')-xc-cd-cm
        d = n.count('D')-cd
        m = n.count('M')-cm
        return 1*i+5*v+10*x+50*l+100*c+500*d+1000*m+4*iv+9*ix+40*xl+90*xc+400*cd+900*cm
