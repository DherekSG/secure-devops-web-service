# 🚀 Secure DevOps Web Service

## 📌 Visão Geral
Este projeto demonstra a implementação completa de um ambiente **DevOps + DevSecOps**, com foco em automação, segurança e boas práticas de infraestrutura.

A solução simula um ambiente real de produção, incluindo:
- Deploy em cloud
- Pipeline CI/CD
- Containerização
- Reverse proxy
- Hardening de servidor
- Monitoramento

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é demonstrar na prática:

- Automação de deploy (CI/CD)
- Uso de containers (Docker)
- Configuração de infraestrutura em cloud
- Aplicação de boas práticas de segurança
- Monitoramento e observabilidade

Este projeto foi desenvolvido como portfólio para atuação em áreas como:
- DevOps
- Cloud Engineer
- Segurança da Informação (Blue Team / SOC)

---

## 🧱 Arquitetura do Sistema

```
[ Usuário ]
     ↓
[ NGINX (porta 80) ]
     ↓
[ FastAPI (porta 8000 - interno) ]
     ↓
[ Docker Containers ]
     ↓
[ VM - Google Cloud ]
```

### Componentes:

- **NGINX:** Atua como proxy reverso
- **FastAPI:** Backend da aplicação
- **Docker:** Isolamento e execução dos serviços
- **GitHub Actions:** Pipeline CI/CD
- **VM (Google Cloud):** Infraestrutura

---

## ⚙️ Pipeline CI/CD (Detalhado)

### Fluxo:

1. Desenvolvedor realiza `git push`
2. GitHub Actions é acionado automaticamente
3. Runner cria ambiente temporário
4. Pipeline executa:
   - Checkout do código
   - Configuração do SSH
   - Conexão com a VM
5. Na VM:
   - Atualiza repositório (`git pull`)
   - Derruba containers antigos
   - Reconstrói containers
   - Sobe nova versão automaticamente

### Tecnologias usadas:

- GitHub Actions
- SSH automatizado
- Docker Compose

---

## 🐳 Containerização (Docker)

### Serviços:

- **fastapi-app** → API principal
- **nginx-proxy** → Proxy reverso
- **netdata** → Monitoramento

### Benefícios aplicados:

- Isolamento de serviços
- Reprodutibilidade do ambiente
- Facilidade de deploy

---

## 🌐 NGINX (Proxy Reverso)

Funções implementadas:

- Receber requisições externas (porta 80)
- Redirecionar para aplicação interna
- Ocultar a porta interna da API

### Benefícios:

- Segurança
- Abstração da aplicação
- Base para HTTPS

---

## 🔐 Segurança (DevSecOps)

### 🔹 Firewall (UFW)

Portas liberadas:

- 22 → SSH
- 80 → HTTP
- 443 → HTTPS (preparado)
- 19999 → Monitoramento

Porta interna protegida:

- 8000 → API (não exposta)

---

### 🔹 Fail2Ban

- Proteção contra ataques de força bruta
- Bloqueio automático após tentativas falhas
- Monitoramento de logs do SSH

---

### 🔹 Hardening SSH

- Login root desativado
- Autenticação por senha desativada
- Apenas autenticação via chave SSH

---

## 📊 Monitoramento e Observabilidade

### Netdata

- Monitoramento em tempo real
- Métricas:
  - CPU
  - Memória
  - Rede
  - Processos

### Logs

#### Docker
```bash
docker logs -f fastapi-app
```

#### Sistema
```bash
sudo journalctl -u ssh
```

#### Fail2Ban
```bash
sudo fail2ban-client status sshd
```

---

## 🌐 Endpoints da Aplicação

- `/` → Status geral
- `/health` → Health check
- `/status` → Informações da aplicação

---

## 🧪 Testes

```bash
curl http://35.223.41.229
curl http://35.223.41.229/health
curl http://35.223.41.229/status
```

---

## 📈 Principais Conceitos Demonstrados

- CI/CD na prática
- Deploy automatizado em cloud
- Arquitetura com containers
- Reverse proxy com NGINX
- Segurança em ambiente Linux
- Monitoramento de aplicação
- Logs e observabilidade

---

## 🚀 Melhorias Futuras

- Implementação de HTTPS (Let's Encrypt)
- Integração com SIEM (Wazuh + ELK)
- Sistema de alertas
- Deploy sem downtime
- Automação com Terraform

---

## 👨‍💻 Autor

Dherek S

DevOps | Cloud | Segurança da Informação

---

## ⭐ Considerações

Este projeto simula um ambiente próximo ao de produção, demonstrando habilidades práticas em:

- Infraestrutura
- Automação
- Segurança
- Observabilidade

Focado em evolução para áreas de:
- DevOps
- Cloud Engineering
- Cybersecurity (Blue Team)
