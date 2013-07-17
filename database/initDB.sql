CREATE TABLE TestRun
(
  creationTimestamp timestamp without time zone DEFAULT timezone('UTC'::text, now()),
  testRunID uuid,
  SN text,
  siteID text,
  stationID text,
  startTimestamp timestamp without time zone,
  endTimestamp timestamp without time zone,
  isPass boolean,
  lastTestEntered text,
  CONSTRAINT TestRun_pkey PRIMARY KEY (testRunID)
);

CREATE TABLE TestMeasurement
(
  creationTimestamp timestamp without time zone DEFAULT timezone('UTC'::text, now()),
  testRunID uuid,
  startTimestamp timestamp without time zone,
  endTimestamp timestamp without time zone,
  testName text,
  testMeasurementName text,
  dataType text,
  stringMin text,
  stringMeasurement text,
  stringMax text,
  doubleMin numeric,
  doubleMeasurement numeric,
  doubleMax numeric,
  isPass boolean
);

CREATE TABLE stringDictionary
(
  creationTimestamp timestamp without time zone DEFAULT timezone('UTC'::text, now()),
  testRunID uuid,
  key text,
  value text
);

CREATE TABLE doubleDictionary
(
  creationTimestamp timestamp without time zone DEFAULT timezone('UTC'::text, now()),
  testRunID uuid,
  key text,
  value numeric
);

CREATE TABLE fileDictionary
(
  creationTimestamp timestamp without time zone DEFAULT timezone('UTC'::text, now()),
  testRunID uuid,
  key text,
  value text
);
