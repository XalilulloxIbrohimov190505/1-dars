class Alisa:
    def hisobla(self,misol):
        print(eval(str(misol)))
    def javob_ber(self,savol):
        if 'isming nima'in savol.lower():
            print('Ismim Alice')
        elif 'yoshing' in savol.lower():
            print('Men 2017-yili yaratilganaman')
        elif 'maziling' in savol.lower():
            print('Germaniya')
        else:
            print('Savolingizga tushunmadim')
al = Alisa()
al. javob_ber('Sening yashash maziling qayer')
al.hisobla('17**3')
