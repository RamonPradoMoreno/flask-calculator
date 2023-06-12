INSERT INTO user (username, password)
VALUES (
    'test',
    'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'
  ),
  (
    'other',
    'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79'
  );
INSERT INTO post (title, body, author_id, created)
VALUES (
    'test title',
    'test body',
    1,
    '2018-01-01 00:00:00'
  );
INSERT INTO history (
    created,
    operation,
    left_operand,
    right_operand,
    result
  )
VALUES ('2023-01-01 00:00:00', 'addition', 1, 2, 3),
  ('2023-01-02 00:00:00', 'addition', -1, -1, -2),
  ('2023-01-03 00:00:00', 'addition', 1, -1, 0),
  -- Maximum precision example
  (
    '2023-01-04 00:00:00',
    'addition',
    0.00000000001,
    0.00000000001,
    0.00000000002
  );