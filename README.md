Trabalho – Padrão de Projeto: Proxy
1. Introdução aos Padrões de Projeto (GoF)
Os padrões de projeto descritos pela Gang of Four (GoF) ajudam a resolver problemas recorrentes em projetos orientados a objetos. Eles trazem soluções reutilizáveis, melhoram a comunicação entre desenvolvedores e tornam o código mais flexível e fácil de manter.
2. Categoria do Padrão Proxy
O padrão Proxy pertence ao grupo de padrões estruturais. Segundo os slides estudados, os padrões estruturais descrevem como objetos e classes podem ser combinados para formar estruturas maiores mantendo flexibilidade e eficiência.
3. Propósito do Padrão Proxy
O padrão Proxy fornece um objeto substituto que controla o acesso a outro objeto. É útil quando desejamos adicionar comportamentos extras ao acessar um objeto real, como controle de acesso, logging, cache, lazy load ou comunicação remota.
4. Problema que o Proxy Resolve
Em diversos casos, não queremos que o código cliente acesse diretamente um objeto complexo, pesado ou sensível. O Proxy atua como intermediário, protegendo o objeto real e adicionando lógica adicional sem modificar o código já existente.
6. Tipos de Proxy Comuns
- Proxy Virtual: cria objetos sob demanda (lazy load)
- Proxy de Proteção: controla permissões de acesso
- Proxy Remoto: representa objetos em outro servidor
- Proxy Cache: armazena resultados para evitar recomputação
7. Vantagens do Proxy
- Controle total sobre o acesso ao objeto real
- Permite criar objetos sob demanda, economizando recursos
- Pode adicionar comportamentos sem alterar o código existente
- Útil para cache, logging e segurança
8. Desvantagens do Proxy
- Aumenta a complexidade do código
- Pode adicionar atrasos devido à camada intermediária
- Em alguns casos, pode ser confundido com Decorator
9. Conclusão
O padrão Proxy é extremamente útil em sistemas que precisam controlar acesso, melhorar performance ou proteger recursos sensíveis. Ele oferece flexibilidade, mantém o princípio da responsabilidade única e permite adicionar comportamentos sem alterar o objeto real.

Slides da disciplina – Engenharia de Software II
GOF – Design Patterns (1994)
