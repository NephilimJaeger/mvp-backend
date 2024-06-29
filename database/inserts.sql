-- Carga inicial de dados

-- Inserindo dados na tabela de professores
INSERT INTO professor (nome, cpf, telefone, endereco, email, data_nascimento, informacoes_adicionais) VALUES ('Paulo Soares Lima', '12345678901', '19998745671', 'Rua do Limoeiro,1756-Bosque','paulo.s.lima@hotmail.com','1989-10-24','Formado em Educação Física pela Unicamp, atua há seis anos como professor de tênis e possui certificações da Federação Internacional de Tênis (ITF) para beach tennis. Ele começou sua carreira no tênis, mas ao se especializar em beach tennis, combinou sua paixão pelo esporte com técnicas avançadas de ensino, destacando-se na formação de novos talentos.');
INSERT INTO professor (nome, cpf, telefone, endereco, email, data_nascimento, informacoes_adicionais) VALUES ('Ana Souza Oliveira', '36457123902', '19923415112', 'Rua UM ,5562 - Centro','ana.s.oliveira@gmail.com','1992-02-10','Ana Souza é uma jogadora profissional de beach tennis que se destaca tanto nas competições quanto em suas aulas e clínicas que promove pelo país. Com certificações da Federação Internacional de Tênis (ITF), Ana combina sua experiência de atleta com técnicas pedagógicas avançadas para ensinar o esporte. Além de competir, é uma referência no ensino do esporte, contribuindo para a formação de novos talentos e promovendo a modalidade.');

-- Inserindo dados na tabela de turmas

INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('12345678901', 'básico', '19:00:00', 'segunda-feira');
INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('36457123902', 'intermediário', '20:00:00', 'segunda-feira');
INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('36457123902', 'intermediário', '21:00:00', 'segunda-feira');
INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('12345678901', 'básico', '19:00:00', 'terça-feira');
INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('12345678901', 'básico', '20:00:00', 'terça-feira');
INSERT INTO turma (id_professor, nivel, horario, dia_semana) VALUES ('36457123902', 'intermediário', '21:00:00', 'terça-feira');

-- Inserindo dados na tabela de alunos

INSERT INTO alunos (nome, cpf, telefone, endereco, data_nascimento, email) VALUES ('Amanda Julia Barbosa', '01737421014', '17984526514', 'Rua das Camélias, 213 - Jardins','2000-02-21','amanda.julia@gmail.com');

-- Inserindo dados na tabela de matriculas

INSERT INTO matricula (id_aluno, id_turma) VALUES ('01737421014', '3');
INSERT INTO matricula (id_aluno, id_turma) VALUES ('01737421014', '6');

