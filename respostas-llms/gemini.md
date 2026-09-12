# Resposta — Gemini

Com base exclusivamente no código-fonte fornecido, os requisitos funcionais e não funcionais efetivamente implementados são:

Requisitos Funcionais (RF)

RF01 - Alternância entre tela de Login e tela de Sistema: O sistema oculta a seção de login e exibe a interface principal ao submeter o formulário de login, realizando o processo inverso ao clicar no botão "Sair".

RF02 - Seleção simulada de Perfil: O formulário de login permite escolher o perfil de acesso (Administrador, Docente ou Estudante) por meio de um campo de seleção (<select>).

RF03 - Exibição do Perfil ativo: O sistema exibe o nome amigável do perfil selecionado (Administrador, Docente ou Estudante) no cabeçalho da aplicação.

RF04 - Menu de Navegação Dinâmico por Perfil: O menu lateral renderiza opções de navegação específicas conforme o perfil selecionado (exibe "Usuários", "Cursos", "Disciplinas" e "Materiais didáticos" para Admin; "Minhas disciplinas" e "Materiais didáticos" para Docente; e "Minhas disciplinas" para Estudante).

RF05 - Navegação entre Telas: O sistema permite alternar o conteúdo principal clicando nos botões do menu lateral, destacando visualmente o item selecionado.

RF06 - Exibição do Dashboard (Visão Geral): O sistema apresenta cartões de métricas estáticas e listagem de disciplinas na tela inicial, variando os rótulos e métricas conforme o perfil (Admin vs. Docente/Estudante).

RF07 - Visualização da Lista de Usuários: A tela de Usuários exibe uma tabela estática contendo Nome, Perfil, E-mail e Status de três usuários predefinidos.

RF08 - Visualização da Lista de Cursos: A tela de Cursos exibe cartões com informações estáticas de cursos predefinidos.

RF09 - Visualização da Lista de Disciplinas: A tela de Disciplinas exibe uma tabela estática com Disciplina, Curso, Responsável, quantidade de Materiais e Status de Acesso.

RF10 - Visualização da Lista de Materiais Didáticos: A tela de Materiais Didáticos exibe cartões com materiais estáticos e uma área reservada simulando conteúdo externo incorporado.

RF11 - Acesso ao Detalhe da Disciplina: Ao clicar no botão "Acessar disciplina", o sistema carrega uma visão detalhada da disciplina selecionada, exibindo cabeçalho personalizado, materiais associados e informações gerais estáticas.

Requisitos Não Funcionais (RNF)

RNF01 - Interface Web Single-Page Application (SPA) em Front-end Puro: Toda a interface e dinâmica de telas são construídas em HTML5, CSS3 e JavaScript (ES6+), sem consumo de APIs de backend, uso de banco de dados ou recarregamento de página.

RNF02 - Design Responsivo: O CSS utiliza media queries (pontos de quebra em 900px e 700px) para reorganizar o layout em telas menores, ajustando o grid de conteúdos, empilhando o cabeçalho/menu e ocultando o rodapé e pills.

RNF03 - Estilização e Tematização Visual: A interface utiliza um tema visual customizado com gradientes, bordas arredondadas, sombras sutis (box-shadow) e tipografia baseada na família Arial/sans-serif.

RNF04 - Estado em Memória: As variáveis de estado da aplicação (role e page) são mantidas apenas na memória da sessão do navegador via JavaScript, sendo redefinidas ao recarregar a página.
