--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application (
    id integer NOT NULL,
    create_date timestamp without time zone,
    target_date character varying NOT NULL,
    cost double precision NOT NULL,
    tg_user_id bigint
);


ALTER TABLE public.application OWNER TO postgres;

--
-- Name: application_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.application_id_seq OWNER TO postgres;

--
-- Name: application_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_id_seq OWNED BY public.application.id;


--
-- Name: applicationcompany; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.applicationcompany (
    id integer NOT NULL,
    id_application bigint,
    company_inn bigint,
    payer_or_recipient_status character varying(15)
);


ALTER TABLE public.applicationcompany OWNER TO postgres;

--
-- Name: applicationcompany_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.applicationcompany_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.applicationcompany_id_seq OWNER TO postgres;

--
-- Name: applicationcompany_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.applicationcompany_id_seq OWNED BY public.applicationcompany.id;


--
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    id integer NOT NULL,
    company_name character varying(100),
    company_inn bigint,
    company_add_date timestamp without time zone,
    tg_user_id bigint
);


ALTER TABLE public.company OWNER TO postgres;

--
-- Name: company_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.company_id_seq OWNER TO postgres;

--
-- Name: company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.company_id_seq OWNED BY public.company.id;


--
-- Name: tguser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tguser (
    id integer NOT NULL,
    tg_user_id bigint,
    tg_username character varying(100) NOT NULL,
    name character varying(100),
    lastname character varying(100)
);


ALTER TABLE public.tguser OWNER TO postgres;

--
-- Name: tguser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tguser_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tguser_id_seq OWNER TO postgres;

--
-- Name: tguser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tguser_id_seq OWNED BY public.tguser.id;


--
-- Name: application id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application ALTER COLUMN id SET DEFAULT nextval('public.application_id_seq'::regclass);


--
-- Name: applicationcompany id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicationcompany ALTER COLUMN id SET DEFAULT nextval('public.applicationcompany_id_seq'::regclass);


--
-- Name: company id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company ALTER COLUMN id SET DEFAULT nextval('public.company_id_seq'::regclass);


--
-- Name: tguser id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tguser ALTER COLUMN id SET DEFAULT nextval('public.tguser_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
265bb89c92c9
\.


--
-- Data for Name: application; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application (id, create_date, target_date, cost, tg_user_id) FROM stdin;
1	2024-03-29 12:20:11	20.10.25	1000	234783286
2	2024-03-29 12:20:11	20.12.25	200000	234783286
3	2024-03-29 12:20:11	20.12.25	200	234783286
4	2024-03-29 12:20:11	20.10.25	2000	234783286
5	2024-03-29 12:20:11	20.04.24	333	436440551
6	2024-03-29 12:20:11	20.10.24	56389	222018626
7	2024-03-30 13:39:20	20.10.25	1000	234783286
8	2024-03-30 13:39:20	30.07.67	56	436440551
9	2024-03-30 13:39:20	04.04.2024	304600	1117366371
10	2024-03-30 13:39:20	09.04.24	670000	153876873
11	2024-03-30 13:39:20	09.04.24	750000	153876873
12	2024-03-30 13:39:20	09.04.24	650000	153876873
13	2024-03-30 13:39:20	09.04.24	780000	153876873
14	2024-03-30 13:39:20	09.04.24	378000	153876873
15	2024-03-30 13:39:20	15.04.24	333500	1449061560
16	2024-03-30 13:39:20	15.04.24	859000	1449061560
17	2024-04-11 17:42:25	15.04.24	100000	328836847
18	2024-04-11 17:42:25	15.04.24	100000	328836847
19	2024-04-11 17:42:25	16.04.24	271333	153876873
20	2024-04-11 17:42:25	18.04.24	940000	153876873
21	2024-04-11 17:42:25	18.04.24	650000	153876873
23	2024-04-11 17:42:25	20.01.25	2	436440551
25	2024-04-11 17:42:25	18.04.24	7000	234783286
26	2024-04-11 17:42:25	19.04.24	475000	397943112
27	2024-04-11 17:42:25	18.04.2024	300000	328836847
28	2024-04-11 17:42:25	19.04.2024	407300	1117366371
\.


--
-- Data for Name: applicationcompany; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.applicationcompany (id, id_application, company_inn, payer_or_recipient_status) FROM stdin;
1	1	1234567891	payer
2	1	123456789123	recipient
3	2	1234567891	payer
4	2	123456789123	recipient
5	3	1234567891	payer
6	3	123456789123	recipient
7	4	1234567891	payer
8	4	123456789123	recipient
9	5	1213123123	payer
10	5	565656643212	recipient
11	6	6354829475	payer
12	6	638502746183	recipient
13	7	1234567891	payer
14	7	123456789123	recipient
15	8	1236541234	payer
16	8	223432345432	recipient
17	9	7733620488	payer
18	9	772600914557	recipient
19	10	7728375424	payer
20	10	440124578778	recipient
21	11	7728375424	payer
22	11	711607502489	recipient
23	12	7728375424	payer
24	12	632133810973	recipient
25	13	7728375424	payer
26	13	772864127383	recipient
27	14	7728375424	payer
28	14	504109272885	recipient
29	15	7718952930	payer
30	15	632123736008	recipient
31	16	7718952930	payer
32	16	772352018416	recipient
33	17	7704349908	payer
34	17	772776248886	recipient
35	18	9718188612	payer
36	18	772776248886	recipient
37	19	7728375424	payer
38	19	504109272885	recipient
39	20	7728375424	payer
40	20	772864127383	recipient
41	21	7728375424	payer
42	21	711607502489	recipient
43	23	3434343434	payer
44	23	343434343434	recipient
45	25	1234567890	payer
46	25	123456789120	recipient
47	26	7714939790	payer
48	26	635704494336	recipient
49	27	7704349908	payer
50	27	772776248886	recipient
51	28	7733620488	payer
52	28	772600914557	recipient
\.


--
-- Data for Name: company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.company (id, company_name, company_inn, company_add_date, tg_user_id) FROM stdin;
1	\N	1234567891	2024-03-29 12:20:11	234783286
2	\N	123456789123	2024-03-29 12:20:11	234783286
3	\N	1213123123	2024-03-29 12:20:11	436440551
4	\N	565656643212	2024-03-29 12:20:11	436440551
5	\N	6354829475	2024-03-29 12:20:11	222018626
6	\N	638502746183	2024-03-29 12:20:11	222018626
7	\N	1236541234	2024-03-30 13:39:20	436440551
8	\N	223432345432	2024-03-30 13:39:20	436440551
9	\N	7733620488	2024-03-30 13:39:20	1117366371
10	\N	772600914557	2024-03-30 13:39:20	1117366371
11	\N	7728375424	2024-03-30 13:39:20	153876873
12	\N	440124578778	2024-03-30 13:39:20	153876873
13	\N	711607502489	2024-03-30 13:39:20	153876873
14	\N	632133810973	2024-03-30 13:39:20	153876873
15	\N	772864127383	2024-03-30 13:39:20	153876873
16	\N	504109272885	2024-03-30 13:39:20	153876873
17	\N	7718952930	2024-03-30 13:39:20	1449061560
18	\N	632123736008	2024-03-30 13:39:20	1449061560
19	\N	772352018416	2024-03-30 13:39:20	1449061560
20	\N	7704349908	2024-04-11 17:42:25	328836847
21	\N	772776248886	2024-04-11 17:42:25	328836847
22	\N	9718188612	2024-04-11 17:42:25	328836847
23	\N	3434343434	2024-04-11 17:42:25	436440551
24	\N	343434343434	2024-04-11 17:42:25	436440551
25	\N	1234567890	2024-04-11 17:42:25	234783286
26	\N	123456789120	2024-04-11 17:42:25	234783286
27	\N	7714939790	2024-04-11 17:42:25	397943112
28	\N	635704494336	2024-04-11 17:42:25	397943112
\.


--
-- Data for Name: tguser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tguser (id, tg_user_id, tg_username, name, lastname) FROM stdin;
1	234783286	def_misha_work	Misha	\N
2	436440551	LegalTechHacker	Boris	\N
3	222018626	uliana_stiagailo	Uliana	Stiagailo
4	132613408	nrthbnd	Nastya	\N
5	1117366371	finshridam	@FINSHRIDAM	\N
6	5503334381	kxiufqr	搬运工代发	@LLE3690
7	153876873	Arthur_315	Arthur	\N
8	1449061560	martyanova_a	Анна	Мартьянова
9	328836847	timofeyshestakov	Тимофей	Шестаков
10	397943112	iukash	Ekaterina	Yukash
11	5406835	LLIuza	Галина Лазарева	@lliuza
\.


--
-- Name: application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_id_seq', 28, true);


--
-- Name: applicationcompany_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.applicationcompany_id_seq', 52, true);


--
-- Name: company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.company_id_seq', 28, true);


--
-- Name: tguser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tguser_id_seq', 11, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: application application_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pkey PRIMARY KEY (id);


--
-- Name: applicationcompany applicationcompany_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicationcompany
    ADD CONSTRAINT applicationcompany_pkey PRIMARY KEY (id);


--
-- Name: company company_company_inn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_company_inn_key UNIQUE (company_inn);


--
-- Name: company company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);


--
-- Name: tguser tguser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tguser
    ADD CONSTRAINT tguser_pkey PRIMARY KEY (id);


--
-- Name: tguser tguser_tg_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tguser
    ADD CONSTRAINT tguser_tg_user_id_key UNIQUE (tg_user_id);


--
-- Name: tguser tguser_tg_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tguser
    ADD CONSTRAINT tguser_tg_username_key UNIQUE (tg_username);


--
-- Name: application application_tg_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_tg_user_id_fkey FOREIGN KEY (tg_user_id) REFERENCES public.tguser(tg_user_id);


--
-- Name: applicationcompany applicationcompany_company_inn_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicationcompany
    ADD CONSTRAINT applicationcompany_company_inn_fkey FOREIGN KEY (company_inn) REFERENCES public.company(company_inn);


--
-- Name: applicationcompany applicationcompany_id_application_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicationcompany
    ADD CONSTRAINT applicationcompany_id_application_fkey FOREIGN KEY (id_application) REFERENCES public.application(id);


--
-- Name: company company_tg_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_tg_user_id_fkey FOREIGN KEY (tg_user_id) REFERENCES public.tguser(tg_user_id);


--
-- PostgreSQL database dump complete
--

