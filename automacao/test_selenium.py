import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://analista-teste.seatecnologia.com.br/"

class TesteSEA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    # CT-002 - Campos obrigatorios
    def test_01_campos_obrigatorios(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)

        btn_adicionar = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'Adicionar Funcionário')]")
            )
        )
        btn_adicionar.click()
        time.sleep(3)

        btn_salvar = driver.find_elements(
            By.XPATH, "//*[contains(text(), 'Salvar') or contains(text(), 'salvar')]"
        )
        if btn_salvar:
            btn_salvar[0].click()
            time.sleep(2)

        assert "Adicionar Funcionário" in driver.page_source, \
            "FALHOU: Formulario enviado sem campos obrigatorios"
        print("CT-002 PASSOU: Campos obrigatorios validados!")

    # CT-003 - CPF invalido
    def test_02_cpf_invalido(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)

        btn_adicionar = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'Adicionar Funcionário')]")
            )
        )
        btn_adicionar.click()
        time.sleep(3)

        # Busca todos os inputs da pagina
        inputs = driver.find_elements(By.XPATH, "//input")
        print(f"Inputs encontrados: {len(inputs)}")

        if len(inputs) >= 1:
            inputs[0].send_keys("João Teste")  # Nome
        if len(inputs) >= 2:
            inputs[1].send_keys("111.111.111-11")  # CPF invalido
        time.sleep(1)

        btn_salvar = driver.find_elements(
            By.XPATH, "//*[contains(text(), 'Salvar') or contains(text(), 'salvar')]"
        )
        if btn_salvar:
            btn_salvar[0].click()
            time.sleep(2)

        page = driver.page_source
        if "CPF inválido" in page or "cpf inválido" in page or "inválido" in page:
            print("CT-003 PASSOU: CPF inválido rejeitado!")
        else:
            print("BUG-005 CONFIRMADO: CPF inválido foi aceito sem validação!")

    # CT-006 - Persistencia de dados
    def test_03_persistencia_dados(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)

        btn_adicionar = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'Adicionar Funcionário')]")
            )
        )
        btn_adicionar.click()
        time.sleep(3)

        try:
            inputs = driver.find_elements(By.XPATH, "//input")
            print(f"Inputs encontrados: {len(inputs)}")

            for i, inp in enumerate(inputs):
                tipo = inp.get_attribute("type")
                nome = inp.get_attribute("name") or inp.get_attribute("placeholder") or f"input_{i}"
                print(f"Input {i}: type={tipo}, name/placeholder={nome}")

            if len(inputs) >= 1:
                inputs[0].send_keys("Teste Automatizado")
            if len(inputs) >= 2:
                inputs[1].send_keys("98765432100")

            data_inputs = driver.find_elements(By.XPATH, "//input[@type='date']")
            if data_inputs:
                data_inputs[0].send_keys("01011990")

            btn_salvar = driver.find_elements(
                By.XPATH, "//*[contains(text(), 'Salvar') or contains(text(), 'salvar')]"
            )
            if btn_salvar:
                btn_salvar[0].click()
                time.sleep(3)

            if "Teste Automatizado" in driver.page_source:
                print("CT-006 PASSOU: Dados salvos e persistidos!")
            else:
                print("CT-006 FALHOU: Dados não aparecem na lista!")

        except Exception as e:
            print(f"CT-006 ERRO: {str(e)}")

    # CT-010 - Navegacao menu lateral
    def test_04_navegacao_menu(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)

        itens_menu = driver.find_elements(
            By.XPATH, "//nav//a | //aside//a | //nav//button | //aside//button"
        )

        if len(itens_menu) == 0:
            print("BUG-012 CONFIRMADO: Menu lateral sem links clicáveis!")
        else:
            for i, item in enumerate(itens_menu):
                try:
                    item.click()
                    time.sleep(1)
                    if "Em breve" in driver.page_source or "em breve" in driver.page_source:
                        print(f"CT-010 Item {i+1} PASSOU: Redirecionou para 'Em breve'")
                    else:
                        print(f"BUG-012 Item {i+1}: Não redirecionou para 'Em breve'")
                except:
                    print(f"BUG-012 Item {i+1}: Não foi possível clicar")

if __name__ == "__main__":
    unittest.main(verbosity=2)