PGDMP     4                     z            store #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1) #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16384    store    DATABASE     w   CREATE DATABASE store WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE store;
                postgres    false            �            1259    16496    data1    TABLE     �   CREATE TABLE public.data1 (
    id integer NOT NULL,
    title character varying,
    herf character varying,
    image character varying,
    rating character varying,
    price character varying,
    location character varying,
    amenities text
);
    DROP TABLE public.data1;
       public         heap    postgres    false            �            1259    16494    test11_id_seq    SEQUENCE     �   CREATE SEQUENCE public.test11_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.test11_id_seq;
       public          postgres    false    221            �           0    0    test11_id_seq    SEQUENCE OWNED BY     >   ALTER SEQUENCE public.test11_id_seq OWNED BY public.data1.id;
          public          postgres    false    220            V           2604    16499    data1 id    DEFAULT     e   ALTER TABLE ONLY public.data1 ALTER COLUMN id SET DEFAULT nextval('public.test11_id_seq'::regclass);
 7   ALTER TABLE public.data1 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221            �          0    16496    data1 
   TABLE DATA           [   COPY public.data1 (id, title, herf, image, rating, price, location, amenities) FROM stdin;
    public          postgres    false    221          �           0    0    test11_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.test11_id_seq', 10, true);
          public          postgres    false    220            X           2606    16504    data1 data1_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.data1
    ADD CONSTRAINT data1_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.data1 DROP CONSTRAINT data1_pkey;
       public            postgres    false    221            �   �  x����n�6���Sh5Y$ER�+m:3	�I�:��h��hK�L4=��}��F�}�>I�;�H J�H߹�W(���^S��������kkT�[���ҚҚ��L��m��<��X}�f�I��V�'�Mj��AW�{q�p�L��L�W{��'��$F{���޷�CTBL
��T��"%X$<,��ԥ�N	��*]/*��xW8�p��ZG,a�Gk�迿���o)����.>W�F�U����u|[���I|t�=��Z����Mp��4��#�U�����on�$���y	�s�!�2>_�]\]��:K�L��l��\
���B$$~�g��&<�7	��#w�`�y�o��|�׍�櫬�=jl���H��A��0n�}v>�$�!�+v���5T���!*�g�q,O��r	0�Rv	
��g�d�8:�����Ť���
ve]`��)S�תQ�~Sp�J�W�ÓbAǐK�9��Ii��2�5�;j&3���?��H>R��_�f���H�h�6�u�m��v�$<d���P�P��^ٹ��j�W� ��mP\���kST�����{�g��GWzS�島�md�Gm�S޺�A��v�8L*����92�,�,#
�L�1�$;�baϞ�e�_	�݄G�J����e?�é+O�ط��0ȿ��|����OG�S�\�L��3MSJ0M��﷧(��|�=y�ڵ�6��?7��汕"�Y-U�v���:_ş�H��x7��b�	%�_N`!a�;\�# �X����0݇6�6SBj�|��6���~�h�T����R�mQ��֛��z�j5@�Z�j�^!!᳍_�sǝ#H1,s����! �8M
��S a��� ��QC��T��u��u�GmV�����4��I=��Z���΍D A�iL)�j��	���]J9C"�cJ�)�m�ǝ�tg?L =��Z��*(i�ԍߓ�d�?D�B�     