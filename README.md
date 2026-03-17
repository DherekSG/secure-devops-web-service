
# 🚀 Secure DevOps Web Service (Production-Ready DevSecOps Project)

## 📌 Visão Geral

Este projeto demonstra a construção de um ambiente completo de **DevOps + DevSecOps**, simulando um cenário real de produção com foco em:

- Automação de deploy (CI/CD)
- Infraestrutura em cloud (Google Cloud)
- Containerização (Docker)
- Proxy Reverso com NGINX
- Segurança aplicada (hardening + proteção)
- Observabilidade e monitoramento
- HTTPS com certificado válido (Let's Encrypt)

🔴 Diferencial: este projeto não é apenas conceitual — ele está **rodando em produção com acesso público e pipeline ativo**.

---

## 🌐 Acesso ao Ambiente (Live Demo)

🔗 Aplicação (HTTPS):  
https://dherekdevops.ddns.net

🔗 Status da API:  
https://dherekdevops.ddns.net/status

🔗 Health Check:  
https://dherekdevops.ddns.net/health

📊 Monitoramento (Netdata):  
http://dherekdevops.ddns.net:19999

---

## 🧠 Objetivo Técnico

Demonstrar capacidade prática em:

- Construção de infraestrutura cloud
- Deploy automatizado sem intervenção manual
- Segurança aplicada em ambiente Linux
- Troubleshooting de problemas reais
- Integração entre múltiplas tecnologias

---

## 🏗️ Arquitetura do Sistema

```
[ Usuário / Internet ]
        ↓
[ DNS (No-IP) ]
        ↓
[ NGINX (Reverse Proxy + HTTPS TLS 1.3) ]
        ↓
[ FastAPI Backend (porta interna 8000) ]
        ↓
[ Docker Containers ]
        ↓
[ VM Linux - Google Cloud ]
```

---

## 🌐 NGINX (Reverse Proxy)

O NGINX atua como **proxy reverso central da aplicação**, sendo responsável por:

- Receber requisições externas (HTTP/HTTPS)
- Encaminhar tráfego para o backend (FastAPI)
- Ocultar portas internas (ex: 8000)
- Realizar terminação SSL (HTTPS)
- Redirecionar HTTP → HTTPS

### Benefícios implementados:

- 🔐 Aumento da segurança (backend não exposto)
- 🌐 Abstração da aplicação
- ⚡ Melhor controle de tráfego
- 🔒 Base para HTTPS e TLS


---

## ⚙️ Stack Tecnológica

### Cloud & Infraestrutura
- Google Cloud Platform (Compute Engine)
- Linux (Ubuntu)

### Containerização
- Docker
- Docker Compose

### Backend
- FastAPI (Python)

### Proxy / Web Server
- NGINX (Reverse Proxy + SSL)

### CI/CD
- GitHub Actions
- Deploy via SSH automatizado

### Segurança
- UFW (Firewall)
- Fail2Ban
- Hardening SSH

### Monitoramento
- Netdata

### DNS & HTTPS
- No-IP (DNS dinâmico)
- Let's Encrypt (Certbot)

---

## 🔁 Pipeline CI/CD (Fluxo Real)

1. Push no repositório GitHub
2. GitHub Actions executa workflow
3. Pipeline autentica via SSH
4. Atualiza código na VM
5. Derruba containers antigos
6. Rebuild das imagens Docker
7. Deploy automático em produção

✔ Zero intervenção manual  
✔ Deploy contínuo real  

---

## 🐳 Containerização

| Container | Função |
|----------|--------|
| api | Backend FastAPI |
| nginx | Proxy reverso + HTTPS |
| netdata | Monitoramento |

Benefícios aplicados:
- Isolamento de serviços
- Reprodutibilidade
- Escalabilidade base

---

## 🔐 Segurança Implementada

### Firewall (Camada dupla)
- UFW (Linux)
- Regras de firewall no GCP

### Proteções
- SSH apenas por chave (sem senha)
- Root login desativado
- Fail2Ban (proteção contra brute-force)

### Rede
- Porta 8000 isolada (acesso interno apenas)
- Exposição controlada (80, 443, 22)

---

## 🔒 HTTPS (TLS)

- Certificado emitido com Let's Encrypt
- TLS 1.3 ativo
- Redirecionamento automático HTTP → HTTPS
- Integração com NGINX em ambiente Docker

---

## 📊 Observabilidade

### Netdata
Monitoramento em tempo real:

- CPU
- Memória
- Rede
- Containers

### Logs

Docker:
```
docker logs -f fastapi-app
```

Sistema:
```
journalctl -u ssh
```

Fail2Ban:
```
fail2ban-client status sshd
```

---

## 🧪 Testes Realizados

- Deploy automático validado
- Teste de falha (container parado → recovery via CI/CD)
- Validação HTTPS
- Testes de firewall
- Testes de endpoints
- Debug de problemas reais (NGINX, SSL, Docker, rede)

---

## 💡 Desafios Técnicos Resolvidos

- Conflito de portas (Docker vs NGINX)
- Integração SSL em ambiente containerizado
- Firewall em múltiplas camadas (UFW + GCP)
- Problemas de configuração do NGINX
- Debug de pipeline CI/CD
- Troubleshooting em ambiente Linux real

---

## 📈 Diferenciais do Projeto

✔ Ambiente rodando em produção  
✔ CI/CD real funcional  
✔ HTTPS válido com domínio  
✔ Segurança aplicada  
✔ Monitoramento ativo  
✔ Troubleshooting real realizado  

---

## 👨‍💻 Autor

Dherek Schaberle  
DevOps | Cloud | Segurança da Informação

---

## ⭐ Considerações Finais

Este projeto demonstra capacidade prática de:

- Construção de ambientes reais
- Automação de deploy
- Implementação de segurança
- Resolução de problemas em produção

Focado em atuação nas áreas de:

- DevOps
- Cloud Engineering
- Cybersecurity (Blue Team / SOC)
