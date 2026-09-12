# Resposta — Claude

Requisitos Funcionais

Exibe uma tela de login com campos de e-mail, senha e seleção de perfil (Administrador, Docente ou Estudante) e botão "Entrar no sistema". 

Concede acesso ao sistema com base exclusivamente no perfil selecionado no formulário — os valores de e-mail e senha informados não são validados pelo código. 

Permite logout através de um botão que retorna o usuário à tela de login. 

Exibe o nome do perfil autenticado no cabeçalho da área interna (ex: "Administrador"). 

Exibe um menu de navegação lateral cujos itens variam conforme o perfil logado: Administrador vê Visão geral, Usuários, Cursos, Disciplinas e Materiais didáticos; Docente vê Visão geral, Minhas disciplinas e Materiais didáticos; Estudante vê apenas Visão geral e Minhas disciplinas. 

Permite alternar entre as páginas internas sem recarregar a página, atualizando dinamicamente o conteúdo da área principal. 

Destaca visualmente, no menu, o item correspondente à página atualmente selecionada. 

Exibe uma página "Visão geral" com cartões de métricas cujo conteúdo difere por perfil (Administrador: Usuários/Cursos/Disciplinas; Docente/Estudante: Disciplinas/Materiais/Conteúdos externos), além de uma listagem de disciplinas em cartões, cada uma com botão "Acessar disciplina". 

Exibe, no menu do Administrador, uma página "Usuários" com tabela estática (nome, perfil, e-mail, status) de usuários pré-definidos no código. 

Exibe, no menu do Administrador, uma página "Cursos" com listagem de cursos em cartões, cada um com botão "Acessar disciplina" que leva a uma página de detalhe. 

Exibe uma página "Disciplinas" com tabela estática (disciplina, curso, responsável, quantidade de materiais, status de acesso). 

Exibe, nos menus de Administrador e Docente, uma página "Materiais didáticos" com listagem de materiais em cartões, cada um identificado por tipo ("Documento externo" ou "Vídeo externo"). 

Exibe, na página de Materiais didáticos, uma área de "Conteúdo incorporado" reservada para vídeo, áudio ou documento hospedado externamente, com aviso explícito de que o protótipo não realiza upload de arquivos. 

Permite acessar uma página de detalhe de disciplina/curso (a partir do botão "Acessar disciplina" presente nos cartões da Visão geral e da página Cursos), exibindo título, descrição, dois materiais de exemplo e um painel de informações (responsável, disponibilidade de materiais, critério de acesso). 

Requisitos Não Funcionais

Implementação inteiramente client-side (HTML, CSS e JavaScript), sem chamadas a servidor, API ou banco de dados. 

Ausência de mecanismo real de autenticação: qualquer combinação de e-mail e senha é aceita, pois esses campos não são verificados no código. 

Ausência de persistência de dados: todo o estado (perfil ativo, página atual) é mantido apenas em memória (variável JavaScript) e é perdido ao recarregar a página ou fazer logout. 

Layout responsivo, adaptando cabeçalho, navegação e rodapé para telas menores por meio de media queries (breakpoints em 900px e 700px). 

Uso exclusivo de tecnologias nativas — HTML5, CSS3 e JavaScript —, sem frameworks ou bibliotecas externas, conforme indicado no próprio rodapé da interface. 

Interface textual integralmente em português do Brasil. 

Identidade visual padronizada por meio de uma única folha de estilos (style.css), aplicada de forma consistente em todas as páginas. 
