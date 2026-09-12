# Resposta — ChatGPT

Com base exclusivamente no código fornecido, os requisitos efetivamente implementados pelo protótipo são os seguintes. Não considerei funcionalidades que apenas aparecem como texto, rótulo ou descrição, mas que não possuem comportamento implementado.

Requisitos funcionais implementados

RF01 — Exibir tela de acesso: o sistema apresenta uma tela de entrada contendo campos de e-mail, senha e seleção de perfil.

RF02 — Selecionar perfil de acesso: o usuário pode selecionar um dos três perfis disponíveis: Administrador, Docente ou Estudante.

RF03 — Validar preenchimento dos campos de acesso: os campos de e-mail e senha possuem validação HTML5 de preenchimento obrigatório e formato de e-mail.

RF04 — Entrar no sistema: ao acionar o botão de entrada, o sistema oculta a tela de login e apresenta a interface correspondente ao perfil selecionado.

RF05 — Identificar o perfil atual: após a entrada, o sistema apresenta o nome do perfil selecionado na interface.

RF06 — Exibir navegação conforme o perfil: o sistema apresenta menus diferentes para Administrador, Docente e Estudante.

RF07 — Exibir visão geral: o sistema apresenta uma página inicial com indicadores e informações resumidas conforme o perfil de usuário.

RF08 — Exibir indicadores administrativos: para o Administrador, a visão geral apresenta as quantidades de usuários, cursos e disciplinas.

RF09 — Exibir indicadores acadêmicos: para Docente e Estudante, a visão geral apresenta indicadores de disciplinas, materiais e conteúdos externos.

RF10 — Listar usuários: o perfil Administrador pode acessar uma página que apresenta uma tabela com nome, perfil, e-mail e status de usuários.

RF11 — Listar cursos: o perfil Administrador pode acessar uma página contendo cursos disponíveis e a quantidade de disciplinas de cada curso.

RF12 — Listar disciplinas: o sistema apresenta disciplinas, seus respectivos cursos, responsáveis, quantidade de materiais e situação de acesso.

RF13 — Apresentar disciplinas do estudante: quando o perfil é Estudante, a página de disciplinas é apresentada como "Minhas disciplinas".

RF14 — Apresentar disciplinas do docente: quando o perfil é Docente, o menu disponibiliza a opção "Minhas disciplinas".

RF15 — Listar materiais didáticos: o sistema apresenta materiais organizados por disciplina.

RF16 — Classificar materiais por tipo de conteúdo externo: os materiais são identificados como documento externo ou vídeo externo.

RF17 — Apresentar área para conteúdo incorporado: o sistema disponibiliza uma área visual destinada à incorporação de vídeo, áudio ou documento hospedado externamente.

RF18 — Informar que não há upload de arquivos: a interface informa explicitamente que o protótipo não realiza upload de arquivos. Isso é uma característica implementada/documentada na interface, não uma funcionalidade de armazenamento.

RF19 — Acessar uma disciplina: a partir dos cartões apresentados na visão geral, o usuário pode acionar "Acessar disciplina" e visualizar uma página específica da disciplina.

RF20 — Exibir materiais de uma disciplina: a página de uma disciplina apresenta materiais introdutório e em vídeo, identificados como conteúdos externos.

RF21 — Exibir informações da disciplina: a página da disciplina apresenta informações sobre responsável, disponibilidade dos materiais e condição de acesso.

RF22 — Navegar entre as páginas: o usuário pode selecionar as opções do menu lateral para alternar entre as páginas disponíveis para seu perfil.

RF23 — Encerrar a sessão visual: o botão "Sair" oculta a interface do sistema e retorna à tela de entrada.

Requisitos não funcionais implementados

RNF01 — Interface responsiva: a interface adapta seu layout para diferentes larguras de tela por meio de regras CSS @media.

RNF02 — Compatibilidade com HTML5: a aplicação utiliza estrutura HTML5 e recursos nativos de formulários, incluindo type="email" e required.

RNF03 — Interface em português brasileiro: o documento HTML declara lang="pt-BR" e os textos da interface são apresentados em português.

RNF04 — Uso de tecnologias web padrão: o protótipo é implementado utilizando HTML5, CSS3 e JavaScript, conforme também identificado no próprio código da interface.

RNF05 — Navegação sem recarregamento de página: a mudança entre as áreas do sistema ocorre por atualização dinâmica do conteúdo do elemento main, utilizando JavaScript.

RNF06 — Adaptação da navegação para dispositivos menores: em telas de menor largura, o menu lateral passa para uma disposição horizontal com rolagem, enquanto o layout principal passa a ser vertical.

RNF07 — Separação entre estrutura, apresentação e comportamento: o protótipo mantém HTML, CSS e JavaScript em arquivos distintos (index.html, style.css e app.js).

O que não deve ser considerado requisito implementado

É importante fazer esta distinção porque o código é explicitamente um protótipo visual. A própria tela informa que se trata de uma demonstração dos cenários de utilização.

Portanto, não considero implementados, por exemplo:

autenticação real;

validação de usuário e senha contra servidor;

cadastro efetivo de usuários;

edição ou exclusão de usuários;

criação, edição ou exclusão de cursos;

criação, edição ou exclusão de disciplinas;

banco de dados;

persistência de dados;

controle real de permissões;

gerenciamento efetivo de matrícula/vínculo;

upload de arquivos;

armazenamento de materiais;

integração real com vídeos, áudios ou documentos externos;

API/backend;

criptografia de senhas;

recuperação de senha;

controle de sessão no servidor;

registro de atividades;

submissão de atividades pelos estudantes.

Há, por exemplo, uma inconsistência deliberadamente importante entre os rótulos da interface e o comportamento efetivo: a página de usuários é denominada "Cadastro e gerenciamento dos usuários", mas o código apenas exibe uma tabela estática; não há operações de cadastro, alteração ou exclusão. Da mesma forma, "Gerenciamento dos cursos" não implica que exista CRUD de cursos.

Observação técnica importante

O mecanismo de "login" também não autentica o usuário. O formulário simplesmente impede o comportamento padrão do navegador e, ao ser submetido, atribui ao estado da aplicação o perfil selecionado no <select> e mostra o sistema. Não existe verificação dos valores de e-mail ou senha.

Nível de confiança: alta. A lista foi derivada diretamente do comportamento observável no código fornecido, sem acrescentar requisitos presumidos.
