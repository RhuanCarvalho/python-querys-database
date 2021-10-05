from datetime import date
from Consultas.Get_Date import Get_Date
from Save_Convert.Save_to_SQL import Save_to_SQL


class Querys_Evolucao_de_Base_sem_migracao_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------
        

    def evolucao_contratos_cancelados_por_cidades(self): 

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Cidade', 'Contratos_Cancelados']
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010,1,1).strftime(self.dates_.style_date)) 
        # -----------------------------
        
        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                select

                case when (contratos.adesao BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
                case when (upper(cidade.cidade) LIKE '%PATR%') THEN 'PATROCINIO'
                    when (upper(cidade.cidade) LIKE '%PATO%') THEN 'PATOS DE MINAS'
                    when (upper(cidade.cidade) LIKE '%GUIM%') THEN 'GUIMARANIA'
                    when (upper(cidade.cidade) LIKE '%ABAD%') THEN 'ABADIA DOS DOURADOS'
                    when (upper(cidade.cidade) LIKE '%IRA%') THEN 'IRAI DE MINAS'
                    when (upper(cidade.cidade) LIKE '%CRUZ%') THEN 'CRUZEIRO DA FORTALEZA'
                    when (upper(cidade.cidade) LIKE '%VARJ%') THEN 'VARJAO DE MINAS'
                    when (upper(cidade.cidade) LIKE '%OLEG%') THEN 'PRESIDENTE OLEGARIO'
                    when (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
                    when (upper(cidade.cidade) LIKE '%JOAO%') THEN 'JOAO PINHEIRO'
                    when (upper(cidade.cidade) LIKE '%LAGOA%') THEN 'LAGOA FORMOSA'
                    ELSE 'OUTROS'
                end as cidade,
                count(contratos.codcontrato) as contratos_cancelados


                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where contratos.cancelado = 'S'
                and contratos.dt_cancelamento BETWEEN '{}' and '{}'
                and
                (	/*Planos Três Marias*/ contratos.plano_acesso NOT IN (3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
                and
                (/*Planos João "Pinheiro*/ contratos.plano_acesso NOT IN (3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))
      			

                group by 1,2

                '''.format(
                #-----------------
                data_fixa,
                final,
                periodo,
                data_fixa,
                final
                #-----------------
            )


            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC, 1 ASC;'''


        Save_to_SQL.save_querys(complete_query, 'evolucao_base_sem_migracao', 'evolucao_contratos_cancelados_por_cidades_sem_migracao')
        return str(complete_query)

    def evolucao_contratos_criados_por_cidades(self): 

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Cidade', 'Contratos_Criados']
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010,1,1).strftime(self.dates_.style_date)) 
        # -----------------------------
        
        

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                select

                case when (contratos.adesao between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
                case when (upper(cidade.cidade) LIKE '%PATR%') THEN 'PATROCINIO'
                    when (upper(cidade.cidade) LIKE '%PATO%') THEN 'PATOS DE MINAS'
                    when (upper(cidade.cidade) LIKE '%GUIM%') THEN 'GUIMARANIA'
                    when (upper(cidade.cidade) LIKE '%ABAD%') THEN 'ABADIA DOS DOURADOS'
                    when (upper(cidade.cidade) LIKE '%IRA%') THEN 'IRAI DE MINAS'
                    when (upper(cidade.cidade) LIKE '%CRUZ%') THEN 'CRUZEIRO DA FORTALEZA'
                    when (upper(cidade.cidade) LIKE '%VARJ%') THEN 'VARJAO DE MINAS'
                    when (upper(cidade.cidade) LIKE '%OLEG%') THEN 'PRESIDENTE OLEGARIO'
                    when (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
                    when (upper(cidade.cidade) LIKE '%JOAO%') THEN 'JOAO PINHEIRO'
                    when (upper(cidade.cidade) LIKE '%LAGOA%') THEN 'LAGOA FORMOSA'
                    ELSE 'OUTROS'
                end as cidade,
                count(contratos.codcontrato) as contratos_criados


                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where contratos.adesao between '{}' and '{}'

                and
                
                (	/*Planos Três Marias*/ contratos.plano_acesso NOT IN (3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
                and
                (/*Planos João "Pinheiro*/ contratos.plano_acesso NOT IN (3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))
      			

                group by 1,2


                '''.format(
                    #-----------------
                    data_fixa,
                    final,
                    periodo,
                    data_fixa,
                    final
                    #-----------------
                )


            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC, 1 ASC;'''



        Save_to_SQL.save_querys(complete_query, 'evolucao_base_sem_migracao', 'evolucao_contratos_criados_por_cidades_sem_migracao')
        return str(complete_query)

    def evolucao_contratos_criados_e_cancelados_totais(self): 

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Quantidade_Criados', 'Quantidade_Cancelados']
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010,1,1).strftime(self.dates_.style_date)) 
        # -----------------------------
        
        

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                
                select

                case when (contratos.adesao BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as data,
                count(contratos.codcontrato) as quantidade_contratos_criados,
                    (select count(contratos.codcontrato) from public.mk_contratos contratos 
                        inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                        inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)	
                        where 
                            (contratos.cancelado = 'S'and contratos.dt_cancelamento BETWEEN '{}' and '{}')
                        and
                
                        (	/*Planos Três Marias*/ contratos.plano_acesso NOT IN (3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
                        and
                        /*(Planos João "Pinheiro contratos.plano_acesso NOT IN (3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))*/

                        pessoa.id_estrangeiro IS NULL
      			
                    ) as quantidade_contratos_cancelados



                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where 
                    (contratos.adesao between  '{}' and '{}')

                    and
                
                    (	/*Planos Três Marias*/ contratos.plano_acesso NOT IN (3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
                    and
                    /*(Planos João "Pinheiro contratos.plano_acesso NOT IN (3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))*/

                        pessoa.id_estrangeiro IS NULL


                group by 1

                '''.format(
                    #-----------------
                    data_fixa,
                    final,
                    periodo,
                    data_fixa,
                    final,
                    data_fixa,
                    final
                    #-----------------
                )


            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 1 ASC;'''



        Save_to_SQL.save_querys(complete_query, 'evolucao_base_sem_migracao', 'evolucao_contratos_criados_e_cancelados_totais_sem_migracao')
        return str(complete_query)



