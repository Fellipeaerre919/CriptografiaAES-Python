# Criptografia AES com Python

Projeto acadêmico desenvolvido em Python. Implementa criptografia e descriptografia de mensagens utilizando o algoritmo AES no modo CBC.

## 🔐 Sobre o projeto

A aplicação funciona pelo terminal. Permite gerar uma chave AES, criptografar mensagens e descriptografar conteúdos previamente criptografados.

O resultado da criptografia é apresentado em formato hexadecimal. O vetor de inicialização (IV) é armazenado junto ao conteúdo criptografado.

## ⚙️ Funcionalidades

- Geração de chave AES aleatória de 16 bytes.
- Possibilidade de reutilizar chave informada anteriormente.
- Criptografia de mensagens com AES no modo CBC.
- Descriptografia de conteúdos em formato hexadecimal.
- Armazenamento temporário da mensagem criptografada durante a execução.
- Interface interativa pelo terminal.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal.
- **PyCryptodome:** biblioteca utilizada na implementação do AES.
- **AES-CBC:** algoritmo e modo de operação utilizados.
- **Hexadecimal:** representação dos dados criptografados.

## 📦 Instalação

É necessário ter Python instalado.

Instale a dependência:

```bash
pip install pycryptodome
```

Clone o repositório:

```bash
git clone https://github.com/Fellipeaerre919/CriptografiaAES-Python.git
```

Acesse a pasta:

```bash
cd CriptografiaAES-Python
```

## ▶️ Como executar

Execute o arquivo principal:

```bash
python criptografia.py
```

Siga as opções apresentadas no terminal para criptografar ou descriptografar mensagens.

**Senha demonstrativa:** `1234`.

## 🔎 Observações técnicas

- Implementação voltada ao aprendizado de conceitos de criptografia.
- O código utiliza AES no modo CBC.
- A senha de acesso está definida diretamente no código.
- O modo CBC não oferece autenticação ou verificação de integridade dos dados.
- A chave deve ser armazenada com segurança.

**Aviso:** este projeto possui finalidade educacional. Não deve ser utilizado para proteger informações reais ou como sistema de segurança em produção.

---

## 👥 Equipe de desenvolvimento

Projeto desenvolvido em equipe por:

- Fellipe Rodrigues Alves
- Pedro Henrique Santos de Almeida
- Rafael Piña Kasbergen
- Thales Duarte de Oliveira

Desenvolvido como projeto acadêmico para aplicação prática de conceitos de Python e criptografia.
