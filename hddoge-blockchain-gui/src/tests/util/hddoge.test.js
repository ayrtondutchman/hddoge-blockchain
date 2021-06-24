const hddoge = require("../../util/hddoge");

describe("hddoge", () => {
  it("converts number mojo to hddoge", () => {
    const result = hddoge.mojo_to_hddoge(1000000);

    expect(result).toBe(0.000001);
  });
  it("converts string mojo to hddoge", () => {
    const result = hddoge.mojo_to_hddoge("1000000");

    expect(result).toBe(0.000001);
  });
  it("converts number mojo to hddoge string", () => {
    const result = hddoge.mojo_to_hddoge_string(1000000);

    expect(result).toBe("0.000001");
  });
  it("converts string mojo to hddoge string", () => {
    const result = hddoge.mojo_to_hddoge_string("1000000");

    expect(result).toBe("0.000001");
  });
  it("converts number hddoge to mojo", () => {
    const result = hddoge.hddoge_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it("converts string hddoge to mojo", () => {
    const result = hddoge.hddoge_to_mojo("0.000001");

    expect(result).toBe(1000000);
  });
  it("converts number mojo to colouredcoin", () => {
    const result = hddoge.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it("converts string mojo to colouredcoin", () => {
    const result = hddoge.mojo_to_colouredcoin("1000000");

    expect(result).toBe(1000);
  });
  it("converts number mojo to colouredcoin string", () => {
    const result = hddoge.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe("1,000");
  });
  it("converts string mojo to colouredcoin string", () => {
    const result = hddoge.mojo_to_colouredcoin_string("1000000");

    expect(result).toBe("1,000");
  });
  it("converts number colouredcoin to mojo", () => {
    const result = hddoge.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it("converts string colouredcoin to mojo", () => {
    const result = hddoge.colouredcoin_to_mojo("1000");

    expect(result).toBe(1000000);
  });
});
