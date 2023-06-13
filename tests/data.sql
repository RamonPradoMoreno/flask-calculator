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