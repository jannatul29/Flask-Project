PGDMP                          z            store #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1) #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16384    store    DATABASE     w   CREATE DATABASE store WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE store;
                postgres    false            ?            1259    16548    user    TABLE     ?   CREATE TABLE public."user" (
    id integer NOT NULL,
    public_id character varying,
    name character varying,
    password character varying
);
    DROP TABLE public."user";
       public         heap    postgres    false            ?            1259    16546    user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    227            ?           0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    226            V           2604    16551    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    226    227            ?          0    16548    user 
   TABLE DATA           ?   COPY public."user" (id, public_id, name, password) FROM stdin;
    public          postgres    false    227   ?
       ?           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 2, true);
          public          postgres    false    226            X           2606    16556    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    227            ?   ?   x?5ϱN1 ???;?%??$s%?@??V?Ŏc?	N??J|>]?????1iHS?4(?F??-b?ʚ??v?\???I ?n??r???????????Ca?A?h	?AQ-C*?gv??%?#???D???3L?]????Z?Ќ-?????i?u????y???????????v?n4???;ZF6c??#??UYU
BRO??zk??l???<??^M1     