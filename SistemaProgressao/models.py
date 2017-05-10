from django.db import models

# classe usuario
class Usuario(models.Model):
	nome = models.CharField(max_length=90)
	email = models.CharField(max_length=90)
	senha = models.CharField(max_length=90)
	siape = models.IntegerField()

	# retorna nome e siape
	# para preenchimentos de formularios
	def __str__ (self):
		return self.nome, self.siape

# classe dos documentos enviados pelos usuarios
class Documento(models.Model):
	link_pdf = models.FileField(upload_to=None, max_length=255)
	fk_usuario = models.ForeignKey(Usuario)

# classe do historico de movimentacao do usuario
class Historico(models.Model):
	# docsfinal/ é o diretorio para os arquivos 
	link_pdf_final = models.FileField(upload_to='documents/', max_length=255)
	fk_usuario = models.ForeignKey(Usuario)


# 
# desenvolvimentos dos formularios baseados no anexos I, II, III e IV
# 

# informacoes gerais que todos os anexos vao possuir
class InfoGerais(models.Model):
	usuario = models.ForeignKey(Usuario)
	lotacao = models.CharField(max_length=15)
	classe = models.CharField(max_length=15)
	periodo = models.DateField()

	# retorna tudo 
	def preenchimento(self):
		return self.usuario, self.lotacao, self.classe, self.periodo

class AnexoI(models.Model):
	# incluir os valores do arquivo excel enviado pelo flavio
	# anexo i

	### INICIO EIXO 1 ###
	# avaliacao discente
	eixo_1 = models.FloatField('Eixo 1')
	eixo_1_justificacao_comentario = models.TextField('Justificativa/Comentario')

	### INICIO EIXO 2.1 ###
	# atividades de ensino e apoio ao ensino
	# ensino convencional

	# horas de aula (media do per)/semana
	eixo_2_1_a_hora = models.FloatField()
	eixo_2_1_b_hora = models.FloatField()
	eixo_2_1_c_hora = models.FloatField()

	# pontos por hora de aula por semana
	eixo_2_1_a_pontos = models.FloatField()
	eixo_2_1_b_pontos = models.FloatField()
	eixo_2_1_c_pontos = models.FloatField()

	# total pontuacao
	eixo_2_1_a_total = models.FloatField()
	eixo_2_1_b_total = models.FloatField()
	eixo_2_1_c_total = models.FloatField()	

	### INICIO EIXO 2.2 ###
	# orientacao de alunos
	
	# numero
	eixo_2_2_a_num = models.FloatField()
	eixo_2_2_b_num = models.FloatField()
	eixo_2_2_c_num = models.FloatField()
	eixo_2_2_d_num = models.FloatField()
	eixo_2_2_e_num = models.FloatField()
	eixo_2_2_f_num = models.FloatField()
	eixo_2_2_g_num = models.FloatField()
	eixo_2_2_h_num = models.FloatField()
	eixo_2_2_i_num = models.FloatField()
	eixo_2_2_j_num = models.FloatField()
	eixo_2_2_k_num = models.FloatField()

	# pontos por aluno por mes
	eixo_2_2_a_pontos = models.FloatField()
	eixo_2_2_b_pontos = models.FloatField()
	eixo_2_2_c_pontos = models.FloatField()
	eixo_2_2_d_pontos = models.FloatField()
	eixo_2_2_e_pontos = models.FloatField()
	eixo_2_2_f_pontos = models.FloatField()
	eixo_2_2_g_pontos = models.FloatField()
	eixo_2_2_h_pontos = models.FloatField()
	eixo_2_2_i_pontos = models.FloatField()
	eixo_2_2_j_pontos = models.FloatField()
	eixo_2_2_k_pontos = models.FloatField()

	# total
	eixo_2_2_a_total = models.FloatField()
	eixo_2_2_b_total = models.FloatField()
	eixo_2_2_c_total = models.FloatField()
	eixo_2_2_d_total = models.FloatField()
	eixo_2_2_e_total = models.FloatField()
	eixo_2_2_f_total = models.FloatField()
	eixo_2_2_g_total = models.FloatField()
	eixo_2_2_h_total = models.FloatField()
	eixo_2_2_i_total = models.FloatField()
	eixo_2_2_j_total = models.FloatField()
	eixo_2_2_k_total = models.FloatField()

	### INICIO EIXO 2.3 ###
	# participacao em projetos, bancas, comissoes, conselhos e equivalentes
	
	# numero
	eixo_2_3_a_num = models.FloatField()
	eixo_2_3_b_num = models.FloatField()
	eixo_2_3_c_num = models.FloatField()
	eixo_2_3_d_num = models.FloatField()
	eixo_2_3_e_num = models.FloatField()
	eixo_2_3_f_num = models.FloatField()
	eixo_2_3_g_num = models.FloatField()
	eixo_2_3_h_num = models.FloatField()

	# pontos por participacao
	eixo_2_3_a_pontos = models.FloatField()
	eixo_2_3_b_pontos = models.FloatField()
	eixo_2_3_c_pontos = models.FloatField()
	eixo_2_3_d_pontos = models.FloatField()
	eixo_2_3_e_pontos = models.FloatField()
	eixo_2_3_f_pontos = models.FloatField()
	eixo_2_3_g_pontos = models.FloatField()
	eixo_2_3_h_pontos = models.FloatField()

	# total
	eixo_2_3_a_total = models.FloatField()
	eixo_2_3_b_total = models.FloatField()
	eixo_2_3_c_total = models.FloatField()
	eixo_2_3_d_total = models.FloatField()
	eixo_2_3_e_total = models.FloatField()
	eixo_2_3_f_total = models.FloatField()
	eixo_2_3_g_total = models.FloatField()
	eixo_2_3_h_total = models.FloatField()

	### INICIO EIXO 2.4 ###
	# participacao em reunioes e cumprimentos de prazos
	
	# numero
	eixo_2_4_a_num = models.FloatField()
	eixo_2_4_b_num = models.FloatField()

	# pontos
	eixo_2_4_a_pontos = models.FloatField()
	eixo_2_4_b_pontos = models.FloatField()

	# total
	eixo_2_4_a_total = models.FloatField()
	eixo_2_4_b_total = models.FloatField()

	# justificativa / comentario
	eixo_2_justificacao_comentario = models.TextField()

	### INICIO EIXO 3.1 ###
	# atividades de capacitacao
	# participacao em cursos e aprovacao em disciplinas

	# numero
	eixo_3_1_a_num = models.FloatField()
	eixo_3_1_b_num = models.FloatField()
	eixo_3_1_c_num = models.FloatField()
	eixo_3_1_d_num = models.FloatField()
	eixo_3_1_e_num = models.FloatField()
	eixo_3_1_f_num = models.FloatField()
	eixo_3_1_g_num = models.FloatField()
	eixo_3_1_h_num = models.FloatField()

	# pontos por participacao
	eixo_3_1_a_pontos = models.FloatField()
	eixo_3_1_b_pontos = models.FloatField()
	eixo_3_1_c_pontos = models.FloatField()
	eixo_3_1_d_pontos = models.FloatField()
	eixo_3_1_e_pontos = models.FloatField()
	eixo_3_1_f_pontos = models.FloatField()
	eixo_3_1_g_pontos = models.FloatField()
	eixo_3_1_h_pontos = models.FloatField()

	# total
	eixo_3_1_a_total = models.FloatField()
	eixo_3_1_b_total = models.FloatField()
	eixo_3_1_c_total = models.FloatField()
	eixo_3_1_d_total = models.FloatField()
	eixo_3_1_e_total = models.FloatField()
	eixo_3_1_f_total = models.FloatField()
	eixo_3_1_g_total = models.FloatField()
	eixo_3_1_h_total = models.FloatField()

	# justificativa / comentario
	eixo_3_justificacao_comentario = models.TextField()

	### INICIO EIXO 4.1 ###
	# atividades de pesquisa e inovacao tecnologica
	# projeto de pesquisa e desenvolvimento tecnologico 

	# numero 
	eixo_4_1_a_num = models.FloatField()
	eixo_4_1_b_num = models.FloatField()
	eixo_4_1_c_num = models.FloatField()
	eixo_4_1_d_num = models.FloatField()

	# pontos 
	eixo_4_1_a_pontos = models.FloatField()
	eixo_4_1_b_pontos = models.FloatField()
	eixo_4_1_c_pontos = models.FloatField()
	eixo_4_1_d_pontos = models.FloatField()

	# total
	eixo_4_1_a_total = models.FloatField()
	eixo_4_1_b_total = models.FloatField()
	eixo_4_1_c_total = models.FloatField()
	eixo_4_1_d_total = models.FloatField()

	### INICIO EIXO 4.2 ###
	# producao bibliografica

	# numero 
	eixo_4_2_a_num = models.FloatField()
	eixo_4_2_b_num = models.FloatField()
	eixo_4_2_c_num = models.FloatField()
	eixo_4_2_d_num = models.FloatField()
	eixo_4_2_e_num = models.FloatField()
	eixo_4_2_f_num = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_num = models.FloatField()
	eixo_4_2_f_A2_num = models.FloatField()
	eixo_4_2_f_B1_num = models.FloatField()
	eixo_4_2_f_B2_num = models.FloatField()
	eixo_4_2_f_B3_num = models.FloatField()
	eixo_4_2_f_B4_num = models.FloatField()
	eixo_4_2_f_B5_num = models.FloatField()
	eixo_4_2_f_C_num = models.FloatField()

	eixo_4_2_g_num = models.FloatField()
	eixo_4_2_h_num = models.FloatField()
	eixo_4_2_i_num = models.FloatField()
	eixo_4_2_j_num = models.FloatField()
	eixo_4_2_k_num = models.FloatField()
	eixo_4_2_l_num = models.FloatField()
	eixo_4_2_m_num = models.FloatField()
	eixo_4_2_n_num = models.FloatField()
	eixo_4_2_o_num = models.FloatField()
	eixo_4_2_p_num = models.FloatField()
	eixo_4_2_q_num = models.FloatField()
	eixo_4_2_r_num = models.FloatField()
	eixo_4_2_s_num = models.FloatField()

	# pontos 
	eixo_4_2_a_pontos = models.FloatField()
	eixo_4_2_b_pontos = models.FloatField()
	eixo_4_2_c_pontos = models.FloatField()
	eixo_4_2_d_pontos = models.FloatField()
	eixo_4_2_e_pontos = models.FloatField()
	eixo_4_2_f_pontos = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_pontos = models.FloatField()
	eixo_4_2_f_A2_pontos = models.FloatField()
	eixo_4_2_f_B1_pontos = models.FloatField()
	eixo_4_2_f_B2_pontos = models.FloatField()
	eixo_4_2_f_B3_pontos = models.FloatField()
	eixo_4_2_f_B4_pontos = models.FloatField()
	eixo_4_2_f_B5_pontos = models.FloatField()
	eixo_4_2_f_C_pontos = models.FloatField()

	eixo_4_2_g_pontos = models.FloatField()
	eixo_4_2_h_pontos = models.FloatField()
	eixo_4_2_i_pontos = models.FloatField()
	eixo_4_2_j_pontos = models.FloatField()
	eixo_4_2_k_pontos = models.FloatField()
	eixo_4_2_l_pontos = models.FloatField()
	eixo_4_2_m_pontos = models.FloatField()
	eixo_4_2_n_pontos = models.FloatField()
	eixo_4_2_o_pontos = models.FloatField()
	eixo_4_2_p_pontos = models.FloatField()
	eixo_4_2_q_pontos = models.FloatField()
	eixo_4_2_r_pontos = models.FloatField()
	eixo_4_2_s_pontos = models.FloatField()

	# total
	eixo_4_2_a_total = models.FloatField()
	eixo_4_2_b_total = models.FloatField()
	eixo_4_2_c_total = models.FloatField()
	eixo_4_2_d_total = models.FloatField()
	eixo_4_2_e_total = models.FloatField()
	eixo_4_2_f_total = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_total = models.FloatField()
	eixo_4_2_f_A2_total = models.FloatField()
	eixo_4_2_f_B1_total = models.FloatField()
	eixo_4_2_f_B2_total = models.FloatField()
	eixo_4_2_f_B3_total = models.FloatField()
	eixo_4_2_f_B4_total = models.FloatField()
	eixo_4_2_f_B5_total = models.FloatField()
	eixo_4_2_f_C_total = models.FloatField()

	eixo_4_2_g_total = models.FloatField()
	eixo_4_2_h_total = models.FloatField()
	eixo_4_2_i_total = models.FloatField()
	eixo_4_2_j_total = models.FloatField()
	eixo_4_2_k_total = models.FloatField()
	eixo_4_2_l_total = models.FloatField()
	eixo_4_2_m_total = models.FloatField()
	eixo_4_2_n_total = models.FloatField()
	eixo_4_2_o_total = models.FloatField()
	eixo_4_2_p_total = models.FloatField()
	eixo_4_2_q_total = models.FloatField()
	eixo_4_2_r_total = models.FloatField()
	eixo_4_2_s_total = models.FloatField()

	### INICIO EIXO 4.3 ###
	# producao tecnica
	
	# numero 
	eixo_4_3_a_num = models.FloatField()
	eixo_4_3_b_num = models.FloatField()
	eixo_4_3_c_num = models.FloatField()
	eixo_4_3_d_num = models.FloatField()
	eixo_4_3_e_num = models.FloatField()
	eixo_4_3_f_num = models.FloatField()
	eixo_4_3_g_num = models.FloatField()
	eixo_4_3_h_num = models.FloatField()
	eixo_4_3_i_num = models.FloatField()
	eixo_4_3_j_num = models.FloatField()
	eixo_4_3_k_num = models.FloatField()
	eixo_4_3_l_num = models.FloatField()
	eixo_4_3_m_num = models.FloatField()
	eixo_4_3_n_num = models.FloatField()
	eixo_4_3_o_num = models.FloatField()
	eixo_4_3_p_num = models.FloatField()
	eixo_4_3_q_num = models.FloatField()
	eixo_4_3_r_num = models.FloatField()
	eixo_4_3_s_num = models.FloatField()
	eixo_4_3_t_num = models.FloatField()
	eixo_4_3_u_num = models.FloatField()
	eixo_4_3_v_num = models.FloatField()
	eixo_4_3_w_num = models.FloatField()
	eixo_4_3_x_num = models.FloatField()
	eixo_4_3_y_num = models.FloatField()
	eixo_4_3_z_num = models.FloatField()
	eixo_4_3_z2_num = models.FloatField()
	eixo_4_3_z3_num = models.FloatField()
	eixo_4_3_z4_num = models.FloatField()
	eixo_4_3_z5_num = models.FloatField()
	eixo_4_3_z6_num = models.FloatField()
	eixo_4_3_z7_num = models.FloatField()
	eixo_4_3_z8_num = models.FloatField()
	eixo_4_3_z9_num = models.FloatField()
	eixo_4_3_z10_num = models.FloatField()
	eixo_4_3_z11_num = models.FloatField()
	eixo_4_3_z12_num = models.FloatField()

	# pontos 
	eixo_4_3_a_pontos = models.FloatField()
	eixo_4_3_b_pontos = models.FloatField()
	eixo_4_3_c_pontos = models.FloatField()
	eixo_4_3_d_pontos = models.FloatField()
	eixo_4_3_e_pontos = models.FloatField()
	eixo_4_3_f_pontos = models.FloatField()
	eixo_4_3_g_pontos = models.FloatField()
	eixo_4_3_h_pontos = models.FloatField()
	eixo_4_3_i_pontos = models.FloatField()
	eixo_4_3_j_pontos = models.FloatField()
	eixo_4_3_k_pontos = models.FloatField()
	eixo_4_3_l_pontos = models.FloatField()
	eixo_4_3_m_pontos = models.FloatField()
	eixo_4_3_n_pontos = models.FloatField()
	eixo_4_3_o_pontos = models.FloatField()
	eixo_4_3_p_pontos = models.FloatField()
	eixo_4_3_q_pontos = models.FloatField()
	eixo_4_3_r_pontos = models.FloatField()
	eixo_4_3_s_pontos = models.FloatField()
	eixo_4_3_t_pontos = models.FloatField()
	eixo_4_3_u_pontos = models.FloatField()
	eixo_4_3_v_pontos = models.FloatField()
	eixo_4_3_w_pontos = models.FloatField()
	eixo_4_3_x_pontos = models.FloatField()
	eixo_4_3_y_pontos = models.FloatField()
	eixo_4_3_z_pontos = models.FloatField()
	eixo_4_3_z2_pontos = models.FloatField()
	eixo_4_3_z3_pontos = models.FloatField()
	eixo_4_3_z4_pontos = models.FloatField()
	eixo_4_3_z5_pontos = models.FloatField()
	eixo_4_3_z6_pontos = models.FloatField()
	eixo_4_3_z7_pontos = models.FloatField()
	eixo_4_3_z8_pontos = models.FloatField()
	eixo_4_3_z9_pontos = models.FloatField()
	eixo_4_3_z10_pontos = models.FloatField()
	eixo_4_3_z11_pontos = models.FloatField()
	eixo_4_3_z12_pontos = models.FloatField()

	# total 
	eixo_4_3_a_total = models.FloatField()
	eixo_4_3_b_total = models.FloatField()
	eixo_4_3_c_total = models.FloatField()
	eixo_4_3_d_total = models.FloatField()
	eixo_4_3_e_total = models.FloatField()
	eixo_4_3_f_total = models.FloatField()
	eixo_4_3_g_total = models.FloatField()
	eixo_4_3_h_total = models.FloatField()
	eixo_4_3_i_total = models.FloatField()
	eixo_4_3_j_total = models.FloatField()
	eixo_4_3_k_total = models.FloatField()
	eixo_4_3_l_total = models.FloatField()
	eixo_4_3_m_total = models.FloatField()
	eixo_4_3_n_total = models.FloatField()
	eixo_4_3_o_total = models.FloatField()
	eixo_4_3_p_total = models.FloatField()
	eixo_4_3_q_total = models.FloatField()
	eixo_4_3_r_total = models.FloatField()
	eixo_4_3_s_total = models.FloatField()
	eixo_4_3_t_total = models.FloatField()
	eixo_4_3_u_total = models.FloatField()
	eixo_4_3_v_total = models.FloatField()
	eixo_4_3_w_total = models.FloatField()
	eixo_4_3_x_total = models.FloatField()
	eixo_4_3_y_total = models.FloatField()
	eixo_4_3_z_total = models.FloatField()
	eixo_4_3_z2_total = models.FloatField()
	eixo_4_3_z3_total = models.FloatField()
	eixo_4_3_z4_total = models.FloatField()
	eixo_4_3_z5_total = models.FloatField()
	eixo_4_3_z6_total = models.FloatField()
	eixo_4_3_z7_total = models.FloatField()
	eixo_4_3_z8_total = models.FloatField()
	eixo_4_3_z9_total = models.FloatField()
	eixo_4_3_z10_total = models.FloatField()
	eixo_4_3_z11_total = models.FloatField()
	eixo_4_3_z12_total = models.FloatField()

	# justificativa / comentario
	eixo_4_justificacao_comentario = models.TextField()

	### INICIO EIXO 5.1 ###
	# atividades de extensao
	# extensao

	# numero
	eixo_5_1_a_num = models.FloatField()
	eixo_5_1_b_num = models.FloatField()
	eixo_5_1_c_num = models.FloatField()
	eixo_5_1_d_num = models.FloatField()
	eixo_5_1_e_num = models.FloatField()
	eixo_5_1_f_num = models.FloatField()
	eixo_5_1_g_num = models.FloatField()
	eixo_5_1_h_num = models.FloatField()
	eixo_5_1_i_num = models.FloatField()
	eixo_5_1_j_num = models.FloatField()
	eixo_5_1_k_num = models.FloatField()
	eixo_5_1_l_num = models.FloatField()
	eixo_5_1_m_num = models.FloatField()
	eixo_5_1_n_num = models.FloatField()

	# pontos
	eixo_5_1_a_pontos = models.FloatField()
	eixo_5_1_b_pontos = models.FloatField()
	eixo_5_1_c_pontos = models.FloatField()
	eixo_5_1_d_pontos = models.FloatField()
	eixo_5_1_e_pontos = models.FloatField()
	eixo_5_1_f_pontos = models.FloatField()
	eixo_5_1_g_pontos = models.FloatField()
	eixo_5_1_h_pontos = models.FloatField()
	eixo_5_1_i_pontos = models.FloatField()
	eixo_5_1_j_pontos = models.FloatField()
	eixo_5_1_k_pontos = models.FloatField()
	eixo_5_1_l_pontos = models.FloatField()
	eixo_5_1_m_pontos = models.FloatField()
	eixo_5_1_n_pontos = models.FloatField()

	# total
	eixo_5_1_a_total = models.FloatField()
	eixo_5_1_b_total = models.FloatField()
	eixo_5_1_c_total = models.FloatField()
	eixo_5_1_d_total = models.FloatField()
	eixo_5_1_e_total = models.FloatField()
	eixo_5_1_f_total = models.FloatField()
	eixo_5_1_g_total = models.FloatField()
	eixo_5_1_h_total = models.FloatField()
	eixo_5_1_i_total = models.FloatField()
	eixo_5_1_j_total = models.FloatField()
	eixo_5_1_k_total = models.FloatField()
	eixo_5_1_l_total = models.FloatField()
	eixo_5_1_m_total = models.FloatField()
	eixo_5_1_n_total = models.FloatField()

	# justificativa / comentario
	eixo_5_justificacao_comentario = models.TextField()

	# representacao profissional ou orgao de classe
	codigo_a_num = models.FloatField()
	codigo_a_pontos = models.FloatField() # pontos por semestre
	codigo_a_total = models.FloatField()

	# situacoes especiais 
	pontos = models.FloatField()
	total = models.FloatField()

class AnexoII(models.Model):
	# incluir os valores do arquivo excel enviado pelo flavio
	# anexo ii

	# qualificacao docente
	numero = models.FloatField()
	pontos = models.FloatField()
	total = models.FloatField()

	### INICIO EIXO 3.1 ###
	# atividades de capacitacao
	# participacao em cursos e aprovacao em disciplinas
	
	# numero
	eixo_3_1_a_num = models.FloatField()
	eixo_3_1_b_num = models.FloatField()
	eixo_3_1_c_num = models.FloatField()
	eixo_3_1_d_num = models.FloatField()
	eixo_3_1_e_num = models.FloatField()
	eixo_3_1_f_num = models.FloatField()
	eixo_3_1_g_num = models.FloatField()
	eixo_3_1_h_num = models.FloatField()

	# pontos por participacao
	eixo_3_1_a_pontos = models.FloatField()
	eixo_3_1_b_pontos = models.FloatField()
	eixo_3_1_c_pontos = models.FloatField()
	eixo_3_1_d_pontos = models.FloatField()
	eixo_3_1_e_pontos = models.FloatField()
	eixo_3_1_f_pontos = models.FloatField()
	eixo_3_1_g_pontos = models.FloatField()
	eixo_3_1_h_pontos = models.FloatField()

	# total
	eixo_3_1_a_total = models.FloatField()
	eixo_3_1_b_total = models.FloatField()
	eixo_3_1_c_total = models.FloatField()
	eixo_3_1_d_total = models.FloatField()
	eixo_3_1_e_total = models.FloatField()
	eixo_3_1_f_total = models.FloatField()
	eixo_3_1_g_total = models.FloatField()
	eixo_3_1_h_total = models.FloatField()

	# justificativa / comentario
	eixo_3_justificacao_comentario = models.TextField()

	### INICIO EIXO 4.1 ###
	# atividades de pesquisa e inovacao tecnologica
	# projeto de pesquisa e desenvolvimento tecnologico 

	# numero 
	eixo_4_1_a_num = models.FloatField()
	eixo_4_1_b_num = models.FloatField()
	eixo_4_1_c_num = models.FloatField()
	eixo_4_1_d_num = models.FloatField()

	# pontos 
	eixo_4_1_a_pontos = models.FloatField()
	eixo_4_1_b_pontos = models.FloatField()
	eixo_4_1_c_pontos = models.FloatField()
	eixo_4_1_d_pontos = models.FloatField()

	# total
	eixo_4_1_a_total = models.FloatField()
	eixo_4_1_b_total = models.FloatField()
	eixo_4_1_c_total = models.FloatField()
	eixo_4_1_d_total = models.FloatField()

	### INICIO EIXO 4.2 ###
	# producao bibliografica

	# numero 
	eixo_4_2_a_num = models.FloatField()
	eixo_4_2_b_num = models.FloatField()
	eixo_4_2_c_num = models.FloatField()
	eixo_4_2_d_num = models.FloatField()
	eixo_4_2_e_num = models.FloatField()
	eixo_4_2_f_num = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_num = models.FloatField()
	eixo_4_2_f_A2_num = models.FloatField()
	eixo_4_2_f_B1_num = models.FloatField()
	eixo_4_2_f_B2_num = models.FloatField()
	eixo_4_2_f_B3_num = models.FloatField()
	eixo_4_2_f_B4_num = models.FloatField()
	eixo_4_2_f_B5_num = models.FloatField()
	eixo_4_2_f_C_num = models.FloatField()

	eixo_4_2_g_num = models.FloatField()
	eixo_4_2_h_num = models.FloatField()
	eixo_4_2_i_num = models.FloatField()
	eixo_4_2_j_num = models.FloatField()
	eixo_4_2_k_num = models.FloatField()
	eixo_4_2_l_num = models.FloatField()
	eixo_4_2_m_num = models.FloatField()
	eixo_4_2_n_num = models.FloatField()
	eixo_4_2_o_num = models.FloatField()
	eixo_4_2_p_num = models.FloatField()
	eixo_4_2_q_num = models.FloatField()
	eixo_4_2_r_num = models.FloatField()
	eixo_4_2_s_num = models.FloatField()

	# pontos 
	eixo_4_2_a_pontos = models.FloatField()
	eixo_4_2_b_pontos = models.FloatField()
	eixo_4_2_c_pontos = models.FloatField()
	eixo_4_2_d_pontos = models.FloatField()
	eixo_4_2_e_pontos = models.FloatField()
	eixo_4_2_f_pontos = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_pontos = models.FloatField()
	eixo_4_2_f_A2_pontos = models.FloatField()
	eixo_4_2_f_B1_pontos = models.FloatField()
	eixo_4_2_f_B2_pontos = models.FloatField()
	eixo_4_2_f_B3_pontos = models.FloatField()
	eixo_4_2_f_B4_pontos = models.FloatField()
	eixo_4_2_f_B5_pontos = models.FloatField()
	eixo_4_2_f_C_pontos = models.FloatField()

	eixo_4_2_g_pontos = models.FloatField()
	eixo_4_2_h_pontos = models.FloatField()
	eixo_4_2_i_pontos = models.FloatField()
	eixo_4_2_j_pontos = models.FloatField()
	eixo_4_2_k_pontos = models.FloatField()
	eixo_4_2_l_pontos = models.FloatField()
	eixo_4_2_m_pontos = models.FloatField()
	eixo_4_2_n_pontos = models.FloatField()
	eixo_4_2_o_pontos = models.FloatField()
	eixo_4_2_p_pontos = models.FloatField()
	eixo_4_2_q_pontos = models.FloatField()
	eixo_4_2_r_pontos = models.FloatField()
	eixo_4_2_s_pontos = models.FloatField()

	# total
	eixo_4_2_a_total = models.FloatField()
	eixo_4_2_b_total = models.FloatField()
	eixo_4_2_c_total = models.FloatField()
	eixo_4_2_d_total = models.FloatField()
	eixo_4_2_e_total = models.FloatField()
	eixo_4_2_f_total = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_total = models.FloatField()
	eixo_4_2_f_A2_total = models.FloatField()
	eixo_4_2_f_B1_total = models.FloatField()
	eixo_4_2_f_B2_total = models.FloatField()
	eixo_4_2_f_B3_total = models.FloatField()
	eixo_4_2_f_B4_total = models.FloatField()
	eixo_4_2_f_B5_total = models.FloatField()
	eixo_4_2_f_C_total = models.FloatField()

	eixo_4_2_g_total = models.FloatField()
	eixo_4_2_h_total = models.FloatField()
	eixo_4_2_i_total = models.FloatField()
	eixo_4_2_j_total = models.FloatField()
	eixo_4_2_k_total = models.FloatField()
	eixo_4_2_l_total = models.FloatField()
	eixo_4_2_m_total = models.FloatField()
	eixo_4_2_n_total = models.FloatField()
	eixo_4_2_o_total = models.FloatField()
	eixo_4_2_p_total = models.FloatField()
	eixo_4_2_q_total = models.FloatField()
	eixo_4_2_r_total = models.FloatField()
	eixo_4_2_s_total = models.FloatField()

	### INICIO EIXO 4.3 ###
	# producao tecnica
	
	# numero 
	eixo_4_3_a_num = models.FloatField()
	eixo_4_3_b_num = models.FloatField()
	eixo_4_3_c_num = models.FloatField()
	eixo_4_3_d_num = models.FloatField()
	eixo_4_3_e_num = models.FloatField()
	eixo_4_3_f_num = models.FloatField()
	eixo_4_3_g_num = models.FloatField()
	eixo_4_3_h_num = models.FloatField()
	eixo_4_3_i_num = models.FloatField()
	eixo_4_3_j_num = models.FloatField()
	eixo_4_3_k_num = models.FloatField()
	eixo_4_3_l_num = models.FloatField()
	eixo_4_3_m_num = models.FloatField()
	eixo_4_3_n_num = models.FloatField()
	eixo_4_3_o_num = models.FloatField()
	eixo_4_3_p_num = models.FloatField()
	eixo_4_3_q_num = models.FloatField()
	eixo_4_3_r_num = models.FloatField()
	eixo_4_3_s_num = models.FloatField()
	eixo_4_3_t_num = models.FloatField()
	eixo_4_3_u_num = models.FloatField()
	eixo_4_3_v_num = models.FloatField()
	eixo_4_3_w_num = models.FloatField()
	eixo_4_3_x_num = models.FloatField()
	eixo_4_3_y_num = models.FloatField()
	eixo_4_3_z_num = models.FloatField()
	eixo_4_3_z2_num = models.FloatField()
	eixo_4_3_z3_num = models.FloatField()
	eixo_4_3_z4_num = models.FloatField()
	eixo_4_3_z5_num = models.FloatField()
	eixo_4_3_z6_num = models.FloatField()
	eixo_4_3_z7_num = models.FloatField()
	eixo_4_3_z8_num = models.FloatField()
	eixo_4_3_z9_num = models.FloatField()
	eixo_4_3_z10_num = models.FloatField()
	eixo_4_3_z11_num = models.FloatField()
	eixo_4_3_z12_num = models.FloatField()

	# pontos 
	eixo_4_3_a_pontos = models.FloatField()
	eixo_4_3_b_pontos = models.FloatField()
	eixo_4_3_c_pontos = models.FloatField()
	eixo_4_3_d_pontos = models.FloatField()
	eixo_4_3_e_pontos = models.FloatField()
	eixo_4_3_f_pontos = models.FloatField()
	eixo_4_3_g_pontos = models.FloatField()
	eixo_4_3_h_pontos = models.FloatField()
	eixo_4_3_i_pontos = models.FloatField()
	eixo_4_3_j_pontos = models.FloatField()
	eixo_4_3_k_pontos = models.FloatField()
	eixo_4_3_l_pontos = models.FloatField()
	eixo_4_3_m_pontos = models.FloatField()
	eixo_4_3_n_pontos = models.FloatField()
	eixo_4_3_o_pontos = models.FloatField()
	eixo_4_3_p_pontos = models.FloatField()
	eixo_4_3_q_pontos = models.FloatField()
	eixo_4_3_r_pontos = models.FloatField()
	eixo_4_3_s_pontos = models.FloatField()
	eixo_4_3_t_pontos = models.FloatField()
	eixo_4_3_u_pontos = models.FloatField()
	eixo_4_3_v_pontos = models.FloatField()
	eixo_4_3_w_pontos = models.FloatField()
	eixo_4_3_x_pontos = models.FloatField()
	eixo_4_3_y_pontos = models.FloatField()
	eixo_4_3_z_pontos = models.FloatField()
	eixo_4_3_z2_pontos = models.FloatField()
	eixo_4_3_z3_pontos = models.FloatField()
	eixo_4_3_z4_pontos = models.FloatField()
	eixo_4_3_z5_pontos = models.FloatField()
	eixo_4_3_z6_pontos = models.FloatField()
	eixo_4_3_z7_pontos = models.FloatField()
	eixo_4_3_z8_pontos = models.FloatField()
	eixo_4_3_z9_pontos = models.FloatField()
	eixo_4_3_z10_pontos = models.FloatField()
	eixo_4_3_z11_pontos = models.FloatField()
	eixo_4_3_z12_pontos = models.FloatField()

	# total 
	eixo_4_3_a_total = models.FloatField()
	eixo_4_3_b_total = models.FloatField()
	eixo_4_3_c_total = models.FloatField()
	eixo_4_3_d_total = models.FloatField()
	eixo_4_3_e_total = models.FloatField()
	eixo_4_3_f_total = models.FloatField()
	eixo_4_3_g_total = models.FloatField()
	eixo_4_3_h_total = models.FloatField()
	eixo_4_3_i_total = models.FloatField()
	eixo_4_3_j_total = models.FloatField()
	eixo_4_3_k_total = models.FloatField()
	eixo_4_3_l_total = models.FloatField()
	eixo_4_3_m_total = models.FloatField()
	eixo_4_3_n_total = models.FloatField()
	eixo_4_3_o_total = models.FloatField()
	eixo_4_3_p_total = models.FloatField()
	eixo_4_3_q_total = models.FloatField()
	eixo_4_3_r_total = models.FloatField()
	eixo_4_3_s_total = models.FloatField()
	eixo_4_3_t_total = models.FloatField()
	eixo_4_3_u_total = models.FloatField()
	eixo_4_3_v_total = models.FloatField()
	eixo_4_3_w_total = models.FloatField()
	eixo_4_3_x_total = models.FloatField()
	eixo_4_3_y_total = models.FloatField()
	eixo_4_3_z_total = models.FloatField()
	eixo_4_3_z2_total = models.FloatField()
	eixo_4_3_z3_total = models.FloatField()
	eixo_4_3_z4_total = models.FloatField()
	eixo_4_3_z5_total = models.FloatField()
	eixo_4_3_z6_total = models.FloatField()
	eixo_4_3_z7_total = models.FloatField()
	eixo_4_3_z8_total = models.FloatField()
	eixo_4_3_z9_total = models.FloatField()
	eixo_4_3_z10_total = models.FloatField()
	eixo_4_3_z11_total = models.FloatField()
	eixo_4_3_z12_total = models.FloatField()

	# justificativa / comentario
	eixo_4_justificacao_comentario = models.TextField()

class AnexoIII(models.Model):
	# incluir os valores do arquivo excel enviado pelo flavio
	# anexo iii

	### INICIO EIXO 3.1 ###
	# atividades de capacitacao
	# participacao em cursos e aprovacao em disciplinas
	
	# numero
	eixo_3_1_a_num = models.FloatField()
	eixo_3_1_b_num = models.FloatField()
	eixo_3_1_c_num = models.FloatField()
	eixo_3_1_d_num = models.FloatField()
	eixo_3_1_e_num = models.FloatField()
	eixo_3_1_f_num = models.FloatField()
	eixo_3_1_g_num = models.FloatField()
	eixo_3_1_h_num = models.FloatField()

	# pontos por participacao
	eixo_3_1_a_pontos = models.FloatField()
	eixo_3_1_b_pontos = models.FloatField()
	eixo_3_1_c_pontos = models.FloatField()
	eixo_3_1_d_pontos = models.FloatField()
	eixo_3_1_e_pontos = models.FloatField()
	eixo_3_1_f_pontos = models.FloatField()
	eixo_3_1_g_pontos = models.FloatField()
	eixo_3_1_h_pontos = models.FloatField()

	# total
	eixo_3_1_a_total = models.FloatField()
	eixo_3_1_b_total = models.FloatField()
	eixo_3_1_c_total = models.FloatField()
	eixo_3_1_d_total = models.FloatField()
	eixo_3_1_e_total = models.FloatField()
	eixo_3_1_f_total = models.FloatField()
	eixo_3_1_g_total = models.FloatField()
	eixo_3_1_h_total = models.FloatField()

	# justificativa / comentario
	eixo_3_justificacao_comentario = models.TextField()

	### INICIO EIXO 5 ###
	# atividades de desempenho gerencial

	# numero
	eixo_5_1_a_num = models.FloatField()
	eixo_5_1_b_num = models.FloatField()
	eixo_5_1_c_num = models.FloatField()
	eixo_5_1_d_num = models.FloatField()
	eixo_5_1_e_num = models.FloatField()
	eixo_5_1_f_num = models.FloatField()
	eixo_5_1_g_num = models.FloatField()
	eixo_5_1_h_num = models.FloatField()
	eixo_5_1_i_num = models.FloatField()
	eixo_5_1_j_num = models.FloatField()
	eixo_5_1_k_num = models.FloatField()
	eixo_5_1_l_num = models.FloatField()

	# pontos
	eixo_5_1_a_pontos = models.FloatField()
	eixo_5_1_b_pontos = models.FloatField()
	eixo_5_1_c_pontos = models.FloatField()
	eixo_5_1_d_pontos = models.FloatField()
	eixo_5_1_e_pontos = models.FloatField()
	eixo_5_1_f_pontos = models.FloatField()
	eixo_5_1_g_pontos = models.FloatField()
	eixo_5_1_h_pontos = models.FloatField()
	eixo_5_1_i_pontos = models.FloatField()
	eixo_5_1_j_pontos = models.FloatField()
	eixo_5_1_k_pontos = models.FloatField()
	eixo_5_1_l_pontos = models.FloatField()

	# total
	eixo_5_1_a_total = models.FloatField()
	eixo_5_1_b_total = models.FloatField()
	eixo_5_1_c_total = models.FloatField()
	eixo_5_1_d_total = models.FloatField()
	eixo_5_1_e_total = models.FloatField()
	eixo_5_1_f_total = models.FloatField()
	eixo_5_1_g_total = models.FloatField()
	eixo_5_1_h_total = models.FloatField()
	eixo_5_1_i_total = models.FloatField()
	eixo_5_1_j_total = models.FloatField()
	eixo_5_1_k_total = models.FloatField()
	eixo_5_1_l_total = models.FloatField()

	# justificativa / comentario
	eixo_5_justificacao_comentario = models.TextField()

	# avaliacao cargos

	# numero meses
	a_num = models.FloatField()
	b_num = models.FloatField()
	c_num = models.FloatField()
	d_num = models.FloatField()
	e_num = models.FloatField()

	# pontos por mes
	a_pontos = models.FloatField()
	b_pontos = models.FloatField()
	c_pontos = models.FloatField()
	d_pontos = models.FloatField()
	e_pontos = models.FloatField()

	# total
	a_total = models.FloatField()
	b_total = models.FloatField()
	c_total = models.FloatField()
	d_total = models.FloatField()
	e_total = models.FloatField()

	# representacao profissional ou orgao de classe

	# numero
	a_num = models.FloatField()

	# pontos por semestre 
	a_pontos = models.FloatField()

	# total
	total = models.FloatField()

	# em caso de afastamente medico, ou equivalente, 
	# o valor aqui sera o minimo requerido, 60 pontos
	pontuacao_min = models.FloatField()


class AnexoIV(models.Model):
	# incluir os valores do arquivo excel enviado pelo flavio
	# anexo iv

	### INICIO EIXO 1 ###
	# avaliacao discente
	eixo_1 = models.FloatField()
	eixo_1_justificacao_comentario = models.TextField()

	### INICIO EIXO 2.1 ###
	# atividades de ensino e apoio ao ensino
	# ensino convencional

	# horas de aula (media do per)/semana
	eixo_2_1_a_hora = models.FloatField()
	eixo_2_1_b_hora = models.FloatField()
	eixo_2_1_c_hora = models.FloatField()

	# pontos por hora de aula por semana
	eixo_2_1_a_pontos = models.FloatField()
	eixo_2_1_b_pontos = models.FloatField()
	eixo_2_1_c_pontos = models.FloatField()

	# total pontuacao
	eixo_2_1_a_total = models.FloatField()
	eixo_2_1_b_total = models.FloatField()
	eixo_2_1_c_total = models.FloatField()	

	### INICIO EIXO 2.2 ###
	# orientacao de alunos
	
	# numero
	eixo_2_2_a_num = models.FloatField()
	eixo_2_2_b_num = models.FloatField()
	eixo_2_2_c_num = models.FloatField()
	eixo_2_2_d_num = models.FloatField()
	eixo_2_2_e_num = models.FloatField()
	eixo_2_2_f_num = models.FloatField()
	eixo_2_2_g_num = models.FloatField()
	eixo_2_2_h_num = models.FloatField()
	eixo_2_2_i_num = models.FloatField()
	eixo_2_2_j_num = models.FloatField()
	eixo_2_2_k_num = models.FloatField()

	# pontos por aluno por mes
	eixo_2_2_a_pontos = models.FloatField()
	eixo_2_2_b_pontos = models.FloatField()
	eixo_2_2_c_pontos = models.FloatField()
	eixo_2_2_d_pontos = models.FloatField()
	eixo_2_2_e_pontos = models.FloatField()
	eixo_2_2_f_pontos = models.FloatField()
	eixo_2_2_g_pontos = models.FloatField()
	eixo_2_2_h_pontos = models.FloatField()
	eixo_2_2_i_pontos = models.FloatField()
	eixo_2_2_j_pontos = models.FloatField()
	eixo_2_2_k_pontos = models.FloatField()

	# total
	eixo_2_2_a_total = models.FloatField()
	eixo_2_2_b_total = models.FloatField()
	eixo_2_2_c_total = models.FloatField()
	eixo_2_2_d_total = models.FloatField()
	eixo_2_2_e_total = models.FloatField()
	eixo_2_2_f_total = models.FloatField()
	eixo_2_2_g_total = models.FloatField()
	eixo_2_2_h_total = models.FloatField()
	eixo_2_2_i_total = models.FloatField()
	eixo_2_2_j_total = models.FloatField()
	eixo_2_2_k_total = models.FloatField()

	### INICIO EIXO 2.3 ###
	# participacao em projetos, bancas, comissoes, conselhos e equivalentes
	
	# numero
	eixo_2_3_a_num = models.FloatField()
	eixo_2_3_b_num = models.FloatField()
	eixo_2_3_c_num = models.FloatField()
	eixo_2_3_d_num = models.FloatField()
	eixo_2_3_e_num = models.FloatField()
	eixo_2_3_f_num = models.FloatField()
	eixo_2_3_g_num = models.FloatField()
	eixo_2_3_h_num = models.FloatField()

	# pontos por participacao
	eixo_2_3_a_pontos = models.FloatField()
	eixo_2_3_b_pontos = models.FloatField()
	eixo_2_3_c_pontos = models.FloatField()
	eixo_2_3_d_pontos = models.FloatField()
	eixo_2_3_e_pontos = models.FloatField()
	eixo_2_3_f_pontos = models.FloatField()
	eixo_2_3_g_pontos = models.FloatField()
	eixo_2_3_h_pontos = models.FloatField()

	# total
	eixo_2_3_a_total = models.FloatField()
	eixo_2_3_b_total = models.FloatField()
	eixo_2_3_c_total = models.FloatField()
	eixo_2_3_d_total = models.FloatField()
	eixo_2_3_e_total = models.FloatField()
	eixo_2_3_f_total = models.FloatField()
	eixo_2_3_g_total = models.FloatField()
	eixo_2_3_h_total = models.FloatField()

	### INICIO EIXO 2.4 ###
	# participacao em reunioes e cumprimentos de prazos
	
	# numero
	eixo_2_4_a_num = models.FloatField()
	eixo_2_4_b_num = models.FloatField()

	# pontos
	eixo_2_4_a_pontos = models.FloatField()
	eixo_2_4_b_pontos = models.FloatField()

	# total
	eixo_2_4_a_total = models.FloatField()
	eixo_2_4_b_total = models.FloatField()

	# justificativa / comentario
	eixo_2_justificacao_comentario = models.TextField()

	### INICIO EIXO 3.1 ###
	# atividades de capacitacao
	# participacao em cursos e aprovacao em disciplinas

	# numero
	eixo_3_1_a_num = models.FloatField()
	eixo_3_1_b_num = models.FloatField()
	eixo_3_1_c_num = models.FloatField()
	eixo_3_1_d_num = models.FloatField()
	eixo_3_1_e_num = models.FloatField()
	eixo_3_1_f_num = models.FloatField()
	eixo_3_1_g_num = models.FloatField()
	eixo_3_1_h_num = models.FloatField()

	# pontos por participacao
	eixo_3_1_a_pontos = models.FloatField()
	eixo_3_1_b_pontos = models.FloatField()
	eixo_3_1_c_pontos = models.FloatField()
	eixo_3_1_d_pontos = models.FloatField()
	eixo_3_1_e_pontos = models.FloatField()
	eixo_3_1_f_pontos = models.FloatField()
	eixo_3_1_g_pontos = models.FloatField()
	eixo_3_1_h_pontos = models.FloatField()

	# total
	eixo_3_1_a_total = models.FloatField()
	eixo_3_1_b_total = models.FloatField()
	eixo_3_1_c_total = models.FloatField()
	eixo_3_1_d_total = models.FloatField()
	eixo_3_1_e_total = models.FloatField()
	eixo_3_1_f_total = models.FloatField()
	eixo_3_1_g_total = models.FloatField()
	eixo_3_1_h_total = models.FloatField()

	# justificativa / comentario
	eixo_3_justificacao_comentario = models.TextField()

	### INICIO EIXO 4.1 ###
	# atividades de pesquisa e inovacao tecnologica
	# projeto de pesquisa e desenvolvimento tecnologico 

	# numero 
	eixo_4_1_a_num = models.FloatField()
	eixo_4_1_b_num = models.FloatField()
	eixo_4_1_c_num = models.FloatField()
	eixo_4_1_d_num = models.FloatField()

	# pontos 
	eixo_4_1_a_pontos = models.FloatField()
	eixo_4_1_b_pontos = models.FloatField()
	eixo_4_1_c_pontos = models.FloatField()
	eixo_4_1_d_pontos = models.FloatField()

	# total
	eixo_4_1_a_total = models.FloatField()
	eixo_4_1_b_total = models.FloatField()
	eixo_4_1_c_total = models.FloatField()
	eixo_4_1_d_total = models.FloatField()

	### INICIO EIXO 4.2 ###
	# producao bibliografica

	# numero 
	eixo_4_2_a_num = models.FloatField()
	eixo_4_2_b_num = models.FloatField()
	eixo_4_2_c_num = models.FloatField()
	eixo_4_2_d_num = models.FloatField()
	eixo_4_2_e_num = models.FloatField()
	eixo_4_2_f_num = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_num = models.FloatField()
	eixo_4_2_f_A2_num = models.FloatField()
	eixo_4_2_f_B1_num = models.FloatField()
	eixo_4_2_f_B2_num = models.FloatField()
	eixo_4_2_f_B3_num = models.FloatField()
	eixo_4_2_f_B4_num = models.FloatField()
	eixo_4_2_f_B5_num = models.FloatField()
	eixo_4_2_f_C_num = models.FloatField()

	eixo_4_2_g_num = models.FloatField()
	eixo_4_2_h_num = models.FloatField()
	eixo_4_2_i_num = models.FloatField()
	eixo_4_2_j_num = models.FloatField()
	eixo_4_2_k_num = models.FloatField()
	eixo_4_2_l_num = models.FloatField()
	eixo_4_2_m_num = models.FloatField()
	eixo_4_2_n_num = models.FloatField()
	eixo_4_2_o_num = models.FloatField()
	eixo_4_2_p_num = models.FloatField()
	eixo_4_2_q_num = models.FloatField()
	eixo_4_2_r_num = models.FloatField()
	eixo_4_2_s_num = models.FloatField()

	# pontos 
	eixo_4_2_a_pontos = models.FloatField()
	eixo_4_2_b_pontos = models.FloatField()
	eixo_4_2_c_pontos = models.FloatField()
	eixo_4_2_d_pontos = models.FloatField()
	eixo_4_2_e_pontos = models.FloatField()
	eixo_4_2_f_pontos = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_pontos = models.FloatField()
	eixo_4_2_f_A2_pontos = models.FloatField()
	eixo_4_2_f_B1_pontos = models.FloatField()
	eixo_4_2_f_B2_pontos = models.FloatField()
	eixo_4_2_f_B3_pontos = models.FloatField()
	eixo_4_2_f_B4_pontos = models.FloatField()
	eixo_4_2_f_B5_pontos = models.FloatField()
	eixo_4_2_f_C_pontos = models.FloatField()

	eixo_4_2_g_pontos = models.FloatField()
	eixo_4_2_h_pontos = models.FloatField()
	eixo_4_2_i_pontos = models.FloatField()
	eixo_4_2_j_pontos = models.FloatField()
	eixo_4_2_k_pontos = models.FloatField()
	eixo_4_2_l_pontos = models.FloatField()
	eixo_4_2_m_pontos = models.FloatField()
	eixo_4_2_n_pontos = models.FloatField()
	eixo_4_2_o_pontos = models.FloatField()
	eixo_4_2_p_pontos = models.FloatField()
	eixo_4_2_q_pontos = models.FloatField()
	eixo_4_2_r_pontos = models.FloatField()
	eixo_4_2_s_pontos = models.FloatField()

	# total
	eixo_4_2_a_total = models.FloatField()
	eixo_4_2_b_total = models.FloatField()
	eixo_4_2_c_total = models.FloatField()
	eixo_4_2_d_total = models.FloatField()
	eixo_4_2_e_total = models.FloatField()
	eixo_4_2_f_total = models.FloatField()
	# valores dentro do codigo f - qualis:
	eixo_4_2_f_A1_total = models.FloatField()
	eixo_4_2_f_A2_total = models.FloatField()
	eixo_4_2_f_B1_total = models.FloatField()
	eixo_4_2_f_B2_total = models.FloatField()
	eixo_4_2_f_B3_total = models.FloatField()
	eixo_4_2_f_B4_total = models.FloatField()
	eixo_4_2_f_B5_total = models.FloatField()
	eixo_4_2_f_C_total = models.FloatField()

	eixo_4_2_g_total = models.FloatField()
	eixo_4_2_h_total = models.FloatField()
	eixo_4_2_i_total = models.FloatField()
	eixo_4_2_j_total = models.FloatField()
	eixo_4_2_k_total = models.FloatField()
	eixo_4_2_l_total = models.FloatField()
	eixo_4_2_m_total = models.FloatField()
	eixo_4_2_n_total = models.FloatField()
	eixo_4_2_o_total = models.FloatField()
	eixo_4_2_p_total = models.FloatField()
	eixo_4_2_q_total = models.FloatField()
	eixo_4_2_r_total = models.FloatField()
	eixo_4_2_s_total = models.FloatField()

	### INICIO EIXO 4.3 ###
	# producao tecnica
	
	# numero 
	eixo_4_3_a_num = models.FloatField()
	eixo_4_3_b_num = models.FloatField()
	eixo_4_3_c_num = models.FloatField()
	eixo_4_3_d_num = models.FloatField()
	eixo_4_3_e_num = models.FloatField()
	eixo_4_3_f_num = models.FloatField()
	eixo_4_3_g_num = models.FloatField()
	eixo_4_3_h_num = models.FloatField()
	eixo_4_3_i_num = models.FloatField()
	eixo_4_3_j_num = models.FloatField()
	eixo_4_3_k_num = models.FloatField()
	eixo_4_3_l_num = models.FloatField()
	eixo_4_3_m_num = models.FloatField()
	eixo_4_3_n_num = models.FloatField()
	eixo_4_3_o_num = models.FloatField()
	eixo_4_3_p_num = models.FloatField()
	eixo_4_3_q_num = models.FloatField()
	eixo_4_3_r_num = models.FloatField()
	eixo_4_3_s_num = models.FloatField()
	eixo_4_3_t_num = models.FloatField()
	eixo_4_3_u_num = models.FloatField()
	eixo_4_3_v_num = models.FloatField()
	eixo_4_3_w_num = models.FloatField()
	eixo_4_3_x_num = models.FloatField()
	eixo_4_3_y_num = models.FloatField()
	eixo_4_3_z_num = models.FloatField()
	eixo_4_3_z2_num = models.FloatField()
	eixo_4_3_z3_num = models.FloatField()
	eixo_4_3_z4_num = models.FloatField()
	eixo_4_3_z5_num = models.FloatField()
	eixo_4_3_z6_num = models.FloatField()
	eixo_4_3_z7_num = models.FloatField()
	eixo_4_3_z8_num = models.FloatField()
	eixo_4_3_z9_num = models.FloatField()
	eixo_4_3_z10_num = models.FloatField()
	eixo_4_3_z11_num = models.FloatField()
	eixo_4_3_z12_num = models.FloatField()

	# pontos 
	eixo_4_3_a_pontos = models.FloatField()
	eixo_4_3_b_pontos = models.FloatField()
	eixo_4_3_c_pontos = models.FloatField()
	eixo_4_3_d_pontos = models.FloatField()
	eixo_4_3_e_pontos = models.FloatField()
	eixo_4_3_f_pontos = models.FloatField()
	eixo_4_3_g_pontos = models.FloatField()
	eixo_4_3_h_pontos = models.FloatField()
	eixo_4_3_i_pontos = models.FloatField()
	eixo_4_3_j_pontos = models.FloatField()
	eixo_4_3_k_pontos = models.FloatField()
	eixo_4_3_l_pontos = models.FloatField()
	eixo_4_3_m_pontos = models.FloatField()
	eixo_4_3_n_pontos = models.FloatField()
	eixo_4_3_o_pontos = models.FloatField()
	eixo_4_3_p_pontos = models.FloatField()
	eixo_4_3_q_pontos = models.FloatField()
	eixo_4_3_r_pontos = models.FloatField()
	eixo_4_3_s_pontos = models.FloatField()
	eixo_4_3_t_pontos = models.FloatField()
	eixo_4_3_u_pontos = models.FloatField()
	eixo_4_3_v_pontos = models.FloatField()
	eixo_4_3_w_pontos = models.FloatField()
	eixo_4_3_x_pontos = models.FloatField()
	eixo_4_3_y_pontos = models.FloatField()
	eixo_4_3_z_pontos = models.FloatField()
	eixo_4_3_z2_pontos = models.FloatField()
	eixo_4_3_z3_pontos = models.FloatField()
	eixo_4_3_z4_pontos = models.FloatField()
	eixo_4_3_z5_pontos = models.FloatField()
	eixo_4_3_z6_pontos = models.FloatField()
	eixo_4_3_z7_pontos = models.FloatField()
	eixo_4_3_z8_pontos = models.FloatField()
	eixo_4_3_z9_pontos = models.FloatField()
	eixo_4_3_z10_pontos = models.FloatField()
	eixo_4_3_z11_pontos = models.FloatField()
	eixo_4_3_z12_pontos = models.FloatField()

	# total 
	eixo_4_3_a_total = models.FloatField()
	eixo_4_3_b_total = models.FloatField()
	eixo_4_3_c_total = models.FloatField()
	eixo_4_3_d_total = models.FloatField()
	eixo_4_3_e_total = models.FloatField()
	eixo_4_3_f_total = models.FloatField()
	eixo_4_3_g_total = models.FloatField()
	eixo_4_3_h_total = models.FloatField()
	eixo_4_3_i_total = models.FloatField()
	eixo_4_3_j_total = models.FloatField()
	eixo_4_3_k_total = models.FloatField()
	eixo_4_3_l_total = models.FloatField()
	eixo_4_3_m_total = models.FloatField()
	eixo_4_3_n_total = models.FloatField()
	eixo_4_3_o_total = models.FloatField()
	eixo_4_3_p_total = models.FloatField()
	eixo_4_3_q_total = models.FloatField()
	eixo_4_3_r_total = models.FloatField()
	eixo_4_3_s_total = models.FloatField()
	eixo_4_3_t_total = models.FloatField()
	eixo_4_3_u_total = models.FloatField()
	eixo_4_3_v_total = models.FloatField()
	eixo_4_3_w_total = models.FloatField()
	eixo_4_3_x_total = models.FloatField()
	eixo_4_3_y_total = models.FloatField()
	eixo_4_3_z_total = models.FloatField()
	eixo_4_3_z2_total = models.FloatField()
	eixo_4_3_z3_total = models.FloatField()
	eixo_4_3_z4_total = models.FloatField()
	eixo_4_3_z5_total = models.FloatField()
	eixo_4_3_z6_total = models.FloatField()
	eixo_4_3_z7_total = models.FloatField()
	eixo_4_3_z8_total = models.FloatField()
	eixo_4_3_z9_total = models.FloatField()
	eixo_4_3_z10_total = models.FloatField()
	eixo_4_3_z11_total = models.FloatField()
	eixo_4_3_z12_total = models.FloatField()

	# justificativa / comentario
	eixo_4_justificacao_comentario = models.TextField()

	### INICIO EIXO 5 ###
	# atividades de extensao
	# extensao

	# numero
	eixo_5_1_a_num = models.FloatField()
	eixo_5_1_b_num = models.FloatField()
	eixo_5_1_c_num = models.FloatField()
	eixo_5_1_d_num = models.FloatField()
	eixo_5_1_e_num = models.FloatField()
	eixo_5_1_f_num = models.FloatField()
	eixo_5_1_g_num = models.FloatField()
	eixo_5_1_h_num = models.FloatField()
	eixo_5_1_i_num = models.FloatField()
	eixo_5_1_j_num = models.FloatField()
	eixo_5_1_k_num = models.FloatField()
	eixo_5_1_l_num = models.FloatField()
	eixo_5_1_m_num = models.FloatField()
	eixo_5_1_n_num = models.FloatField()

	# pontos
	eixo_5_1_a_pontos = models.FloatField()
	eixo_5_1_b_pontos = models.FloatField()
	eixo_5_1_c_pontos = models.FloatField()
	eixo_5_1_d_pontos = models.FloatField()
	eixo_5_1_e_pontos = models.FloatField()
	eixo_5_1_f_pontos = models.FloatField()
	eixo_5_1_g_pontos = models.FloatField()
	eixo_5_1_h_pontos = models.FloatField()
	eixo_5_1_i_pontos = models.FloatField()
	eixo_5_1_j_pontos = models.FloatField()
	eixo_5_1_k_pontos = models.FloatField()
	eixo_5_1_l_pontos = models.FloatField()
	eixo_5_1_m_pontos = models.FloatField()
	eixo_5_1_n_pontos = models.FloatField()

	# total
	eixo_5_1_a_total = models.FloatField()
	eixo_5_1_b_total = models.FloatField()
	eixo_5_1_c_total = models.FloatField()
	eixo_5_1_d_total = models.FloatField()
	eixo_5_1_e_total = models.FloatField()
	eixo_5_1_f_total = models.FloatField()
	eixo_5_1_g_total = models.FloatField()
	eixo_5_1_h_total = models.FloatField()
	eixo_5_1_i_total = models.FloatField()
	eixo_5_1_j_total = models.FloatField()
	eixo_5_1_k_total = models.FloatField()
	eixo_5_1_l_total = models.FloatField()
	eixo_5_1_m_total = models.FloatField()
	eixo_5_1_n_total = models.FloatField()

	# justificativa / comentario
	eixo_5_justificacao_comentario = models.TextField()

	### INICIO EIXO 5 ###
	# atividades de desempenho gerencial
	# 

	# numero
	eixo_5_1_a_num = models.FloatField()
	eixo_5_1_b_num = models.FloatField()
	eixo_5_1_c_num = models.FloatField()
	eixo_5_1_d_num = models.FloatField()
	eixo_5_1_e_num = models.FloatField()
	eixo_5_1_f_num = models.FloatField()
	eixo_5_1_g_num = models.FloatField()
	eixo_5_1_h_num = models.FloatField()
	eixo_5_1_i_num = models.FloatField()
	eixo_5_1_j_num = models.FloatField()
	eixo_5_1_k_num = models.FloatField()
	eixo_5_1_l_num = models.FloatField()

	# pontos
	eixo_5_1_a_pontos = models.FloatField()
	eixo_5_1_b_pontos = models.FloatField()
	eixo_5_1_c_pontos = models.FloatField()
	eixo_5_1_d_pontos = models.FloatField()
	eixo_5_1_e_pontos = models.FloatField()
	eixo_5_1_f_pontos = models.FloatField()
	eixo_5_1_g_pontos = models.FloatField()
	eixo_5_1_h_pontos = models.FloatField()
	eixo_5_1_i_pontos = models.FloatField()
	eixo_5_1_j_pontos = models.FloatField()
	eixo_5_1_k_pontos = models.FloatField()
	eixo_5_1_l_pontos = models.FloatField()

	# total
	eixo_5_1_a_total = models.FloatField()
	eixo_5_1_b_total = models.FloatField()
	eixo_5_1_c_total = models.FloatField()
	eixo_5_1_d_total = models.FloatField()
	eixo_5_1_e_total = models.FloatField()
	eixo_5_1_f_total = models.FloatField()
	eixo_5_1_g_total = models.FloatField()
	eixo_5_1_h_total = models.FloatField()
	eixo_5_1_i_total = models.FloatField()
	eixo_5_1_j_total = models.FloatField()
	eixo_5_1_k_total = models.FloatField()
	eixo_5_1_l_total = models.FloatField()

	# justificativa / comentario
	eixo_5_justificacao_comentario = models.TextField()

	# avaliacao cargos

	# numero meses
	a_num = models.FloatField()
	b_num = models.FloatField()
	c_num = models.FloatField()
	d_num = models.FloatField()
	e_num = models.FloatField()

	# pontos por mes
	a_pontos = models.FloatField()
	b_pontos = models.FloatField()
	c_pontos = models.FloatField()
	d_pontos = models.FloatField()
	e_pontos = models.FloatField()

	# total
	a_total = models.FloatField()
	b_total = models.FloatField()
	c_total = models.FloatField()
	d_total = models.FloatField()
	e_total = models.FloatField()

	# representacao profissional ou orgao de classe

	# numero
	a_num = models.FloatField()

	# pontos por semestre 
	a_pontos = models.FloatField()

	# total
	total = models.FloatField()

	# em caso de afastamente medico, ou equivalente, 
	# o valor aqui sera o minimo requerido, 60 pontos
	pontuacao_min = models.FloatField()

'''
# tudo isso de linha e é agora que vai realmente começar o trabalho 

o que falta?
	- retorno das funcoes com os valores totais
	- verificar se tudo está ok, sim, ler essas 1500 linhas
	- testar depois

'''
