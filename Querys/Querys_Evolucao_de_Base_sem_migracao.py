from datetime import date
from Consultas.Get_Date import Get_Date


class Querys_Evolucao_de_Base_sem_migracao_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def evolucao_contratos_cancelados_por_cidades(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT
    CASE 
        WHEN (contratos.adesao BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS adesao,
    CASE 
        WHEN (upper(cidade.cidade) LIKE '%PATR%')   THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')   THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')   THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')   THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE 'IRA%')    THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')   THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')   THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')   THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%')     THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%PINHEIRO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')      THEN 'LAGOA FORMOSA'
        WHEN (upper(cidade.cidade) LIKE '%GON%ALO%')  THEN 'SAO GONCALO DO ABAETE'
        WHEN (upper(cidade.cidade) LIKE '%PIRAPORA%')  THEN 'PIRAPORA'
        WHEN (upper(cidade.cidade) LIKE '%V%RZEA%')  THEN 'VARZEA DA PALMA'
        WHEN (upper(cidade.cidade) LIKE '%BURITIZEIRO%')  THEN 'BURITIZEIRO'
        ELSE 'OUTROS'
    END AS cidade,
    COUNT(contratos.codcontrato) AS contratos_cancelados

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    contratos.cancelado = 'S'
    AND contratos.dt_cancelamento BETWEEN '{}' AND '{}'
    AND(/*Planos Três Marias*/ 
        contratos.plano_acesso NOT IN (
            3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
    AND(/*Planos João Pinheiro*/
        contratos.plano_acesso NOT IN (
            3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))
    AND 
        coalesce(pessoa.operadora_fone, '') != 'Migrado06'
    AND
        coalesce(pessoa.operadora_fone, '') != 'Migrado11'

GROUP BY 1,2

            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 2 ASC, 1 ASC;
'''

        return str(complete_query)

    def evolucao_contratos_criados_por_cidades(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT
    CASE 
        WHEN (contratos.adesao BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS adesao,
    CASE
        WHEN (upper(cidade.cidade) LIKE '%PATR%')       THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')       THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')       THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')       THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE 'IRA%')        THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')       THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')       THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')       THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%')     THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%PINHEIRO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')      THEN 'LAGOA FORMOSA'
        WHEN (upper(cidade.cidade) LIKE '%GON%ALO%')    THEN 'SAO GONCALO DO ABAETE'
        WHEN (upper(cidade.cidade) LIKE '%PIRAPORA%')  THEN 'PIRAPORA'
        WHEN (upper(cidade.cidade) LIKE '%V%RZEA%')  THEN 'VARZEA DA PALMA'
        WHEN (upper(cidade.cidade) LIKE '%BURITIZEIRO%')  THEN 'BURITIZEIRO'
        ELSE 'OUTROS'
    END AS cidade,
    COUNT(contratos.codcontrato) AS contratos_criados

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    contratos.adesao BETWEEN '{}' AND '{}'
    AND(/*Planos Três Marias*/ 
        contratos.plano_acesso NOT IN (
            3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420))
    AND(/*Planos João "Pinheiro*/ 
        contratos.plano_acesso NOT IN (
            3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193))
    AND
        coalesce(pessoa.operadora_fone, '') != 'Migrado06'
    AND
        coalesce(pessoa.operadora_fone, '') != 'Migrado11'

GROUP BY 1,2

            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 2 ASC, 1 ASC;
'''

        return str(complete_query)

    def evolucao_contratos_criados_e_cancelados_totais(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
SELECT
    CASE 
        WHEN (contratos.adesao BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS data,
    COUNT(contratos.codcontrato) AS quantidade_contratos_criados,

    -- INICIO
    ( 
    SELECT 
        COUNT (contratos.codcontrato) 
    FROM 
        public.mk_contratos contratos 
        INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
        INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)	
    WHERE 
        (
            contratos.cancelado = 'S' 
            AND contratos.dt_cancelamento BETWEEN '{}' AND '{}')
        AND(/*Planos Três Marias*/ 
            contratos.plano_acesso NOT IN (
                3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420)
            )
        AND( pessoa.id_estrangeiro IS NULL
            /*(Planos João Pinheiro 
            contratos.plano_acesso NOT IN (
                3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193)*/
            )
        AND coalesce(pessoa.operadora_fone, '') != 'Migrado06'
    ) AS quantidade_contratos_cancelados
    -- FIM

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    (contratos.adesao between  '{}' and '{}')
    AND(/*Planos Três Marias*/ 
            contratos.plano_acesso NOT IN (
                3370,3389,3373,3376,3379,3369,3382,3384,3387,3390,3400,3330,3325,3326,3327,3328,3331,3332,3333,3351,3352,3380,3401,3381,3385,3386,3383,3388,3399,3404,3416,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3329,3346,3353,3354,3355,3356,3357,3358,3359,3360,3361,3362,3363,3364,3367,3368,3412,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3349,3393,3402,3403,3413,3414,3415,3394,3405,3417,3418,3419,3421,3420)
        )
    AND( pessoa.id_estrangeiro IS NULL
        /*(Planos João Pinheiro 
        contratos.plano_acesso NOT IN (
            3104,3195,3192,3183,3134,3118,3119,3182,3120,3181,3121,3180,3179,3168,3167,3161,3158,3156,3155,3154,3153,3152,3151,3150,3149,3148,3147,3146,3103,3108,3113,3122,3123,3124,3130,3126,3127,3129,3131,3132,3142,3144,3145,3017,3021,3024,3032,3039,3047,3055,3056,3057,3076,3077,3084,3091,3100,3101,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3054,3018,3019,3020,3022,3023,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3037,3038,3040,3041,3042,3043,3044,3045,3046,3048,3049,3050,3051,3052,3053,3058,3059,3060,3061,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3078,3079,3080,3081,3082,3083,3085,3086,3087,3088,3063,3089,3090,3092,3093,3094,3095,3096,3137,3097,3098,3099,3102,3105,3106,3107,3109,3110,3111,3112,3114,3115,3116,3117,3125,3128,3133,3135,3136,3138,3139,3140,3141,3143,3157,3162,3169,3170,3171,3176,3184,3185,3186,3187,3188,3189,3194,3193)*/
        )
    AND coalesce(pessoa.operadora_fone, '') != 'Migrado06'

GROUP BY 1
              
            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 1 ASC;
'''

        return str(complete_query)
