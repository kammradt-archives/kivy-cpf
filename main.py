from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from func.GeradorCPF import gerador_cpf
from func.GeraListaCPF import GeradorListaCPF
from func.ValidadorCPF import CPF_Valido



class Gerenciador(ScreenManager):
    pass
    # Entidade responsável por controlar as telas

class Menu(Screen):
    pass
    # Menu do usuário

class ValidarCpf(Screen):
    def init(self,**kwargs):
        super().init(**kwargs)

    def chamaValidador(self):
        return CPF_Valido(self.campo_do_cpf_no_cod_python.text)


class GerarCpf(Screen):
    def init(self,**kwargs):
        super().init(**kwargs)

    def chamaGerador(self):
        quantidade = int(self.campo_da_quantidade.text)
        # Vai definir o tipo de retorno

        if quantidade <= 1:
            cpfsGerados = gerador_cpf()
        else:
            cpfsGerados = GeradorListaCPF(quantidade)

        return cpfsGerados


class Principal(App):
    def build(self):
        return Gerenciador()
    # É útil quando existem diversas coisas a serem chamadas
    # Mas por padrão foi utilizado também


# Inicia de fato o app
Principal().run()
