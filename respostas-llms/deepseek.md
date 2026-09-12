# Resposta — DeepSeek

Com base exclusivamente no código fornecido, seguem os requisitos funcionais e não funcionais que a aplicação efetivamente implementa.

Requisitos Funcionais

O sistema apresenta uma tela de login com campos de e-mail, senha e seleção de perfil (Administrador, Docente ou Estudante).

O sistema permite entrar no ambiente principal ao submeter o formulário de login, sem validar credenciais contra backend ou banco de dados.

O sistema permite sair do ambiente principal e retornar à tela de login por meio do botão “Sair”.

O sistema exibe o nome do perfil selecionado no cabeçalho após o login.

O sistema monta o menu de navegação lateral de acordo com o perfil selecionado (admin, teacher ou student).

O sistema permite navegar entre as páginas do menu lateral sem recarregar a página.

O sistema exibe uma página de “Visão geral” com métricas diferentes conforme o perfil: para admin, usuários, cursos e disciplinas; para docente e estudante, disciplinas, materiais e conteúdos externos.

O sistema exibe, na visão geral, cards de disciplinas com título, descrição e quantidade de materiais.

O sistema permite acessar uma disciplina a partir do botão “Acessar disciplina”, exibindo uma página com materiais e informações da disciplina.

O sistema exibe uma página de “Usuários” com tabela contendo nome, perfil, e-mail e status de usuários.

O sistema exibe uma página de “Cursos” com cards de cursos contendo título, descrição e quantidade de disciplinas.

O sistema exibe uma página de “Disciplinas” com tabela contendo disciplina, curso, responsável, quantidade de materiais e status de acesso.

O sistema exibe uma página de “Materiais didáticos” com cards de materiais contendo título, disciplina e tipo (documento externo ou vídeo externo).

O sistema exibe uma área de conteúdo incorporado que informa ser reservada para vídeo, áudio ou documento externo, sem realizar upload de arquivos.

O sistema adapta o título da página de disciplinas para “Minhas disciplinas” quando o perfil é estudante.

O sistema renderiza todo o conteúdo dinamicamente via JavaScript, sem recarregamento de página.

Requisitos Não Funcionais

A aplicação é implementada em HTML5, CSS3 e JavaScript puro, sem frameworks de frontend.

A aplicação é executada inteiramente no navegador, sem backend, banco de dados ou autenticação real.

O layout é responsivo, com ajustes para telas menores que 900px e 700px.

A interface utiliza uma identidade visual própria, com cores, cards, badges e tipografia definidos em CSS.

O sistema é um protótipo visual acadêmico, conforme indicado no rodapé e na tela de login.

A navegação entre páginas é feita por manipulação de estado em JavaScript, sem rotas de URL.

O código não realiza persistência de dados entre sessões ou recarregamentos.
