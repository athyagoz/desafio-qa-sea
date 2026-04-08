from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """
    Page Object para a tela principal da aplicação.
    Contém todos os elementos e ações da tela de listagem
    de funcionários.
    """

    URL = "http://analista-teste.seatecnologia.com.br/"

    # Localizadores dos elementos da página
    BTN_ADICIONAR = (
        By.XPATH,
        "//*[contains(text(), 'Adicionar Funcionário')]"
    )
    BTN_PROXIMO_PASSO = (
        By.XPATH,
        "//*[contains(text(), 'Próximo passo')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        """Abre a página principal da aplicação."""
        self.driver.get(self.URL)

    def clicar_adicionar_funcionario(self):
        """Clica no botão de adicionar funcionário."""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_ADICIONAR)
        )
        btn.click()

    def clicar_proximo_passo(self):
        """Clica no botão próximo passo."""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_PROXIMO_PASSO)
        )
        btn.click()

    def get_itens_menu_lateral(self):
        """Retorna todos os itens do menu lateral."""
        return self.driver.find_elements(
            By.XPATH,
            "//nav//a | //aside//a | //nav//button | //aside//button"
        )

    def funcionario_na_lista(self, nome):
        """Verifica se um funcionário aparece na lista."""
        return nome in self.driver.page_source

    def pagina_carregada(self):
        """Verifica se a página principal carregou."""
        return "Funcionário" in self.driver.page_source
