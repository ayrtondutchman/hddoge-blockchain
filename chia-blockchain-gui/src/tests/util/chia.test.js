const chia = require('../../util/chia');

describe('chia', () => {
  it('converts number pupps to chia', () => {
    const result = chia.pupps_to_chia(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string pupps to chia', () => {
    const result = chia.pupps_to_chia('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number pupps to chia string', () => {
    const result = chia.pupps_to_chia_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string pupps to chia string', () => {
    const result = chia.pupps_to_chia_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number chia to pupps', () => {
    const result = chia.chia_to_pupps(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string chia to pupps', () => {
    const result = chia.chia_to_pupps('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number pupps to colouredcoin', () => {
    const result = chia.pupps_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string pupps to colouredcoin', () => {
    const result = chia.pupps_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number pupps to colouredcoin string', () => {
    const result = chia.pupps_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string pupps to colouredcoin string', () => {
    const result = chia.pupps_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to pupps', () => {
    const result = chia.colouredcoin_to_pupps(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to pupps', () => {
    const result = chia.colouredcoin_to_pupps('1000');

    expect(result).toBe(1000000);
  });
});
