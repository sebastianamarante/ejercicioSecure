class Texto:
    def limpiar(texto):
        quitar = ",;:.\n!\"'}{"
        for caracter in quitar:
            texto = texto.replace(caracter,
                          " ")
                                

        texto = texto.lower()
        palabras = texto.split()
        return palabras

    @classmethod
    def contadorFrecuencia(self, texto):
        diccionario_frecuencias = {}
        for palabras in self.limpiar(texto):
            diccionario_frecuencias[palabras] = diccionario_frecuencias.get(palabras, 0) + 1

        for palabras in list(diccionario_frecuencias):
            if diccionario_frecuencias[palabras] < 2:
                diccionario_frecuencias.pop(palabras)

        return diccionario_frecuencias

    @classmethod
    def top5(self, text, top):
        ranking = sorted(self.contadorFrecuencia(text).items(), key=lambda x: x[1], reverse=True)
        ranking = ranking[0:top]
        return ranking
