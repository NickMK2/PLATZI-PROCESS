class contador:
    
    contador = 0
    
    @classmethod
    def incremento(cls):
        cls.contador += 1
        
contador.incremento()
contador.incremento()
contador.incremento()
print(contador.contador)